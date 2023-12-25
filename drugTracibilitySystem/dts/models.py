from django.db import models

# Create your models here.
class pharmaceuticals(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    
class HealthCenter(models.Model):
    healthcenter_name = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    village = models.CharField(max_length=100)

