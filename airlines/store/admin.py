from django.contrib import admin
from store.models import ProductModel

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "description",
        "stock",
    )
