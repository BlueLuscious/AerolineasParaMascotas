from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'
    verbose_name = _("dashboard")

    def ready(self) -> None:
        
        from .admins import (
            staff_user_admin
        )

        from .models.proxies import (
            staff_user
        )
