from django.apps import AppConfig
from django.contrib import admin
from django.db import models

class ConfigConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'config'

    def ready(self) -> None:
        from .admins import (
            admin,
            palette_admin,
        )

        from .models import (
            models,
            palette_model,
        )
        