from django.apps import AppConfig


class ConfigConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'config'
    verbose_name = "Configuraciones"

    def ready(self) -> None:
        from .admins import (
            admin,
            palette_admin,
        )

        from .models import (
            models,
            palette_model,
        )
        