import logging
from django import template

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("components/atoms/custom-button.html")
def custom_button(
    id:int,
    type:str="button",
    label:str="",
    icon_name:str="",
    classes:str="",
    label_classes:str="",
    icon_classes:str="",
) -> dict:
    context = dict(
        id=id,
        type=type,
        label=label,
        icon_name=icon_name,
        classes=classes,
        label_classes=label_classes,
        icon_classes=icon_classes,
    )
    logger.info(f"custom button context: {context}")
    return context
