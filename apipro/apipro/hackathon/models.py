# app_name/models.py

from django.db import models

class InputData(models.Model):
    date_time = models.DateTimeField()
    battery_temp = models.FloatField()
    voltage = models.FloatField()
    current = models.FloatField()
    wheel_rpm = models.FloatField()
    wheel_temp = models.FloatField()

