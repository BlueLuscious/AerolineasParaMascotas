from django.urls import path
from web.views.index_view import IndexView
from web.views.category_view import CategoryView

urlpatterns = [
    path('index/', IndexView.as_view(), name="index"),
    path('Category/<int:boton_id>/', CategoryView.as_view(), name="Category"),
]
