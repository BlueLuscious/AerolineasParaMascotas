from django.urls import path
from web.views.index_view import IndexView
from web.views.race_distintion_view import RaceDistintionView
from web.views.subcategory_view import SubcategoryView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('sin-distincion-de-raza/', RaceDistintionView.as_view(), name="race-distintion"),
]
