import logging
from django import template

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("components/atoms/grid-card.html")
def grid_card(index:int, classes:str = "", bg_image:str = "", content_image:str = "", label_text:str = "") -> dict:
    context = dict(
        index=index,
        classes=classes,
        bg_image=bg_image,
        content_image=content_image,
        label_text=label_text,
    )
    logger.info(f"category card context: {context}")
    return context
