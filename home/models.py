from django.db import models
from django.utils import timezone

class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=30)
    model_name = models.CharField(max_length=30)
    production_year = models.CharField(max_length=50)
    available_seat = models.IntegerField()
    desc = models.TextField()
    vehicle_color = models.CharField(max_length=30)
    license_plate = models.IntegerField() 
    created_at = models.DateTimeField(default=timezone.now)

    #this means when you call query Vehicle.objects.all() it will appear by its vehicle_name not 'Vehicle objects (1)'\
    # You need to run the shell again to see the result
    def __str__(self): 
        return self.vehicle_name
