from django.db import models

# Create your models here.


class GlobalAirPolutionModel(models.Model):
    aqi = models.CharField(max_length=100, blank=False, null=False)
    co_aqi = models.CharField(max_length=100, blank=False, null=False)
    ozone_aqi = models.CharField(max_length=100, blank=False, null=False)
    no2_aqi = models.CharField(max_length=100, blank=False, null=False)
    pm2_5_aqi = models.CharField(max_length=100, blank=False, null=False)