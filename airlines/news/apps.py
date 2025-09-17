from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class NewsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "news"
    verbose_name = _("news_pl")
    

    def ready(self) -> None:

        from .admins import (
            news_model_admin
        )

        from .models import (
            news_model
        )
        