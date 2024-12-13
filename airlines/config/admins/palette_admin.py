from django.contrib import admin
from config.models.palette_model import PaletteModel


@admin.register(PaletteModel)
class PaletteAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "primary_colour",
        "secondary_colour",
        "terciary_colour",
    )
