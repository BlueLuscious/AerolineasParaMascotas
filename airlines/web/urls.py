from django.urls import path
from web.views.index_view import IndexView
from web.views.race_distintion_view import RaceDistintionView
from web.views.travel_quietly_view import TravelQuietlyView
from web.views.travel_restriction_view import TravelRestrictionView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("sin-distincion-de-raza/", RaceDistintionView.as_view(), name="race-distintion"),
    path("viaja-tranquilo/", TravelQuietlyView.as_view(), name="travel-quietly"),
    path("restricciones-por-raza/", TravelRestrictionView.as_view(), name="travel-restriction"),
]
