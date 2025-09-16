from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class StaffUser(User):
    class Meta:
        proxy = True
        verbose_name = _("staff_user")
        verbose_name_plural = _("staff_users")

    def save(self, *args, **kwargs) -> None:
        self.is_staff = True
        self.is_superuser = False
        return super().save(*args, **kwargs)
    