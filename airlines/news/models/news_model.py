from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class NewsModel(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField(verbose_name=_("content"))
    image = models.ImageField(upload_to="news/", blank=True, null=True, verbose_name=_("image"))
    is_featured = models.BooleanField(default=False, verbose_name=_("is_featured"))
    published = models.BooleanField(default=True, verbose_name=_("published"))
    start_date = models.DateTimeField(blank=True, null=True, verbose_name=_("start_date"))
    end_date = models.DateTimeField(blank=True, null=True, verbose_name=_("end_date"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("news_sing")
        verbose_name_plural = _("news_pl")
        ordering = ["-created_at"]

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    def is_visible(self):
        today = now()
        if not self.published:
            return False
        if self.start_date and today < self.start_date:
            return False
        if self.end_date and today > self.end_date:
            return False
        return True
    