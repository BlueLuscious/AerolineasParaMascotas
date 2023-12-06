from django.contrib import admin
from django.urls import path, include
#.................................
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
]
if settings.DEBUG: #aca pregunto si estoy en debug, ya que nunca me dejaria hacerlo en produccion
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)