from .models import DestinationModel
from django.contrib import admin

@admin.register(DestinationModel)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['country', 'city', 'airport']
    search_fields = ('country', 'city', 'airport',)
    ordering = ['country']
    