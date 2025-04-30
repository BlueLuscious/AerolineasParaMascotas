import logging
from django import template

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("components/atoms/grid-card.html")
def grid_card(
    container_classes: str, classes: str = "", bg_image: str = "", content_image: str = "", label_text: str = "", label_classes: str = ""
) -> dict:
    context = dict(
        container_classes=container_classes,
        classes=classes,
        bg_image=bg_image,
        content_image=content_image,
        label_text=label_text,
        label_classes=label_classes,

    )
    logger.info(f"category card context: {context}")
    return context
