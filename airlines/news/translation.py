from modeltranslation.translator import register, TranslationOptions
from news.models.news_model import NewsModel


@register(NewsModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ("title", "content")
