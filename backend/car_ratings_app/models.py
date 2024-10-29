# car_ratings_app/models.py
from django.db import models

class Car(models.Model):
    model_year = models.TextField(blank=True, null=True)
    make = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    vehicle_description = models.TextField(blank=True, null=True)
    vehicle_id = models.TextField(blank=True, null=True)
    trim = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicles'
