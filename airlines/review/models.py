from django.db import models


class ReviewModel(models.Model):
    image = models.ImageField(upload_to="images/", blank=True, null=True, verbose_name="Imagen")
    stars = models.IntegerField(default=5, verbose_name="Estrellas")
    description = models.CharField(max_length=256, null=True, blank=True, verbose_name="Descripción")
    origin = models.CharField(max_length=128, verbose_name="Origen")
    destination = models.CharField(max_length=128, verbose_name="Destino")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    def __str__(self):
        return f"Calificacion N°{self.pk}"
    