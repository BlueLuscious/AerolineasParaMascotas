from django.urls import path
from web.views.index_view import IndexView
from web.views.quotation_view import QuotationView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("cotizar-traslado/", QuotationView.as_view(), name="quotation"),
]
