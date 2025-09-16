from django.contrib import admin
from django.urls import path, include
#.................................
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("dashboard.urls")),
    path('', include('web.urls')),
    path("unicorn/", include("django_unicorn.urls")),
    path("", include("django_components.urls")),
    path('i18n/', include('django.conf.urls.i18n')),
]
if settings.DEBUG: #aca pregunto si estoy en debug, ya que nunca me dejaria hacerlo en produccion
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    