from django.urls import path
from web.views.index_view import IndexView
from web.views.category_view import CategoryView
from web.views.subcategory_view import SubcategoryView

urlpatterns = [
    path('index/', IndexView.as_view(), name="index"),
    path('Category/<int:boton_id>/', CategoryView.as_view(), name="Category"),
    path('Subcategory/<int:boton_id>/', SubcategoryView.as_view(), name="Subcategory"),
]
