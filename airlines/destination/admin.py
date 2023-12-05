from django.contrib import admin
from .models import DestinationModel

@admin.register(DestinationModel)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['country', 'city', 'airport']
    pass
