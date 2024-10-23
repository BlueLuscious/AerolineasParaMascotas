from django.contrib import admin
from review.models import ReviewModel


@admin.register(ReviewModel)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "stars",
        "origin",
        "destination",
    )
