from django.contrib import admin
from ..models.news_model import NewsModel

@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "title",
        "is_featured",
        "published",
        "start_date",
        "end_date",
    ]
    search_fields = (
        "pk",
        "title",
        "slug",
    )
    fields = [
        "title",
        "title_en",
        "content",
        "content_en",
        "image",
        "is_featured",
        "published",
        "start_date",
        "end_date",
    ]
    ordering = ["-created_at"]
    