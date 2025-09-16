from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _


class StaffAdminSite(AdminSite):
    pass

    def has_permission(self, request) -> bool:
        return request.user.is_active and request.user.is_staff
    

staff_admin_site = StaffAdminSite("staff_admin")
