from django.contrib import admin
from config.models.models import ConfigModel


@admin.register(ConfigModel)
class ConfigAdmin(admin.ModelAdmin):
    list_display = (
        # 'terms_and_conditions',
        'email_contact',
        'active',
    )
#TODO mostrar pdf como en adecash