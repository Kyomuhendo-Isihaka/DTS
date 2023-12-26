from django.db import models

# Create your models here.
    
class HealthCenter(models.Model):
    healthcenter_name = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    village = models.CharField(max_length=100)

class Drug(models.Model):
    DrugID = models.AutoField(primary_key=True)
    DrugName = models.CharField(max_length=255)
    # Manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    BatchNumber = models.CharField(max_length=50)
    ManufacturingDate = models.DateTimeField(auto_now_add=True)
    DrugDescription = models.CharField(max_length=255)
    ExpirationDate = models.DateTimeField()
    Quantity = models.PositiveIntegerField()
   
class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    UserType = models.CharField(max_length=50)
    Phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.UserName} - {self.Phone}"
