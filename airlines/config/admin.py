from django.contrib import admin

from config.models import ConfigModel

# Register your models here.
@admin.register(ConfigModel)
class ConfigAdmin(admin.ModelAdmin):
    list_display = (
        # 'terms_and_conditions',
        'email_contact',
    )
#TODO mostrar pdf como en adecash