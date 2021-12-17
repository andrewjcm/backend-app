from django.db import models


class CovidDeathAgeCount(models.Model):
    age = models.IntegerField(unique=True)
    count = models.IntegerField()


class ComorbidityCounts(models.Model):
    pneumonia = models.IntegerField()
    diabetes = models.IntegerField()
    copd = models.IntegerField()
    asthma = models.IntegerField()
    inmsupr = models.IntegerField()
    hypertension = models.IntegerField()
    other_disease = models.IntegerField()
    cardiovascular = models.IntegerField()
    obesity = models.IntegerField()
    renal_chronic = models.IntegerField()
    tobacco = models.IntegerField()


class SurvivalRate(models.Model):
    rate = models.FloatField()


class HealthProfile(models.Model):
    sex = models.IntegerField()
    patient_type = models.IntegerField(default=0)
    age = models.IntegerField()
    pneumonia = models.IntegerField(default=0)
    diabetes = models.IntegerField(default=0)
    copd = models.IntegerField(default=0)
    asthma = models.IntegerField(default=0)
    inmsupr = models.IntegerField(default=0)
    hypertension = models.IntegerField(default=0)
    other_disease = models.IntegerField(default=0)
    cardiovascular = models.IntegerField(default=0)
    obesity = models.IntegerField(default=0)
    renal_chronic = models.IntegerField(default=0)
    tobacco = models.IntegerField(default=0)
    covid_positive = models.IntegerField(default=1)

    def custom_dict(self):
        new_dict = self.__dict__
        del new_dict['_state']
        del new_dict['id']
        del new_dict['covid_positive']
        return new_dict


class SurvivalPrediction(models.Model):
    died = models.FloatField()
    health_profile_id = models.OneToOneField(HealthProfile, on_delete=models.CASCADE, primary_key=True)
