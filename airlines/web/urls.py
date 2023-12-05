from django.urls import path
from web.views.index_view import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]