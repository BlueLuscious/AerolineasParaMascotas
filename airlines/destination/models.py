from django.db import models

class DestinationModel(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    airport = models.CharField(max_length=100)
    
    def __str__(self): 
        return f"{self.country} - {self.city} - {self.airport} "