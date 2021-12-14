from django.contrib.auth.models import User, Group
from .models import HealthProfile, SurvivalPrediction
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class HealthProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HealthProfile
        fields = [
            'sex',
            'patient_type',
            'age',
            'pneumonia',
            'diabetes',
            'copd',
            'asthma',
            'inmsupr',
            'hypertension',
            'other_disease',
            'cardiovascular',
            'obesity',
            'renal_chronic',
            'tobacco'
        ]


class SurvivalPredictionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SurvivalPrediction
        fields = [
            'died',
            'health_profile_id'
        ]