from django.contrib import admin
from django.contrib.auth.hashers import make_password
from ..models.proxies.staff_user import StaffUser


@admin.register(StaffUser)
class StaffUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_active", "is_superuser", )
    list_filter = ("is_active", )
    search_fields = ("username", "email", )
    fields = ("username", "password", "groups", "user_permissions", "is_active", )

    def save_model(self, request, obj: "StaffUser", form, change) -> None:
        obj.is_staff = True
        obj.is_superuser = False
        obj.password = make_password(obj.password)
        return super().save_model(request, obj, form, change)
