from django.urls import path
from web.views.index_view import IndexView
# from airlines.web.views.category_view import CategoryView

urlpatterns = [
    path('index/', IndexView.as_view(), name="index"),
    # path('Raza/', CategoryView.as_view(), name="index"),
]