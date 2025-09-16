from django.urls import path
from .sites import staff_admin_site


urlpatterns = [
    path("staff-admin/", staff_admin_site.urls),
]
