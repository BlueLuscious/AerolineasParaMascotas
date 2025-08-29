import logging
from django import template

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("components/atoms/bar-item.html")
def nav_item(
    current_path: str, nav_item_url: str, nav_item_content: str, nav_item_ref: str = "", path_name: str = "", nav_item_id: str = ""
) -> dict:
    if nav_item_ref.startswith("#"):
        if current_path == "/":
            href = nav_item_ref
        else:
            href = f"/{nav_item_ref}"
    elif nav_item_ref:
        href = nav_item_ref
    else:
        href = nav_item_url

    context = dict(
        current_path=current_path, 
        path_name=path_name, 
        nav_item_id=nav_item_id, 
        nav_item_content=nav_item_content, 
        href=href,
    )
    logger.info(f"category card context: {context}")
    return context
