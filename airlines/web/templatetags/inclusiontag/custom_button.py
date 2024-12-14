import logging
from django import template

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("components/custom-button.html")
def custom_button(url: str, target: str, label: str, tailwind_class: str = "") -> dict:
    context = {
        "my_url": url,
        "my_target": target,
        "label": label,
        "tailwind_class": tailwind_class,
    }
    logger.info(f"category card context: {context}")
    return context
