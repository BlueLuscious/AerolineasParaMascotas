import logging
from django import template

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("components/custom-button.html")
def custom_button(label: str, url: str = "", target: str= "", type: str = "button", btn_tailwind: str = "") -> dict:
    context = {
        "my_label": label,
        "my_url": url,
        "my_target": target,
        "type": type,
        "btn_tailwind": btn_tailwind,
    }
    logger.info(f"category card context: {context}")
    return context
