from django.db import models

# Create your models here.
class MyTracker(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()