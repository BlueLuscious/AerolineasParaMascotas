from django.db import models

class DestinationModel(models.Model):
    country = models.CharField(max_length=100, verbose_name="País")
    city = models.CharField(max_length=100, verbose_name="Ciudad")
    airport = models.CharField(max_length=100, verbose_name="Aeropuerto")
    image = models.ImageField(upload_to='images/', default='images/default_product.png', blank=True, null=True, verbose_name="Imagen")
    
    def __str__(self): 
        return f"{self.country} - {self.city}"