from django.db import models

# Create your models here.
class Drivers(models.Model):
    D_Name= models.CharField(max_length=100)
    D_EMail= models.EmailField(unique=True)
    D_Phone = models.IntegerField(max_length=12)
    
    def __str__(self):
        return self.D_EMail
    

class Vehicles(models.Model):
    V_Number= models.CharField(max_length=20, unique=True)
    V_Type= models.CharField(max_length=50)
    V_Capacity= models.IntegerField()
    Driver= models.ForeignKey(Drivers, on_delete=models.CASCADE)

    def __str__(self):
        return self.V_Number
    
class Routes(models.Model):
    R_Start= models.CharField(max_length=100)
    R_End= models.CharField(max_length=100)
    R_Distance= models.FloatField()
    Vehicle= models.ForeignKey(Vehicles, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.R_Start} to {self.R_End}"
    
class Deliveries(models.Model):
    D_Item= models.CharField(max_length=200)
    D_Weight= models.FloatField()
    Route= models.ForeignKey(Routes, on_delete=models.CASCADE)
    Delivery_Date= models.DateField()

    def __str__(self):
        return self.D_Item
    
class bookings(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    pickup_location = models.CharField(max_length=200)
    dropoff_location = models.CharField(max_length=200)
    pickup_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    vehicle_type = models.CharField(max_length=50)

    def __str__(self):
        return f"Booking by {self.name} for {self.vehicle_type}"