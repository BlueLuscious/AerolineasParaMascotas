from django.db import models

class ConfigModel(models.Model):
    # name = models.CharField(max_length=200, null=True, blank=True)
    terms_and_conditions = models.FileField(upload_to='terms_and_conditions/', blank=True)
    email_contact = models.CharField(max_length=200, null=True, blank=True) #TODO preguntar si dejamos algun email personal 
    contract = models.FileField(upload_to='contract/', blank=True)
    active = models.BooleanField(default=True)


