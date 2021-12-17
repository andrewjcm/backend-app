from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework import permissions
from .serializers import (
    UserSerializer, GroupSerializer,
    HealthProfileSerializer, SurvivalPredictionSerializer,
    CovidDataSerializer
)
from .models import (
    HealthProfile, SurvivalPrediction,
    CovidDeathAgeCount, ComorbidityCounts,
    SurvivalRate
)

from machine_learning.logistic_reg import PredictSurvival
from data_visualization.data_mod import process_data

from collections import namedtuple

CovidData = namedtuple('CovidData', ('death_age', 'comorbidity', 'survival_rate'))


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CovidDataViewSet(viewsets.ViewSet):
    """
    API endpoint to view the covid data.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = SurvivalRate.objects.all()
        if not queryset:
            processed_data = process_data()
            survival_rate = processed_data['survival_rate']
            death_age = processed_data['died_covid_age']
            comorbidity = processed_data['comorbidity']

            death_age_objs = [CovidDeathAgeCount(age=key, count=death_age[key]) for key in death_age]
            CovidDeathAgeCount.objects.bulk_create(death_age_objs)

            sr = SurvivalRate(rate=survival_rate)
            sr.save()

            com = ComorbidityCounts(**comorbidity)
            com.save()

        covid_data = CovidData(
            death_age=CovidDeathAgeCount.objects.all(),
            comorbidity=ComorbidityCounts.objects.all(),
            survival_rate=SurvivalRate.objects.all()
        )
        serializer = CovidDataSerializer(covid_data)
        return Response(serializer.data)


def create_prediction():
    prof = HealthProfile.objects.all().last()
    prof_id = prof.id
    prof_dict = prof.custom_dict()
    predict = PredictSurvival(prof_dict)
    s = SurvivalPrediction(predict.result, prof_id)
    s.save()
    return s.died


def append_prediction_to_response(data):
    prediction = create_prediction()
    data['died'] = prediction
    return data


class HealthProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows health profiles to be viewed or edited.
    """
    queryset = HealthProfile.objects.all()
    serializer_class = HealthProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        new_data = append_prediction_to_response(serializer.data)
        return Response(new_data, status=status.HTTP_201_CREATED, headers=headers)


class SurvivalPredictionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = SurvivalPrediction.objects.all()
    serializer_class = SurvivalPredictionSerializer
    permission_classes = [permissions.IsAuthenticated]

