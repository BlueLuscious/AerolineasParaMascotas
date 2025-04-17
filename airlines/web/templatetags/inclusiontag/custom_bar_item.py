import logging
from django import template

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("components/atoms/bar-item.html")
def nav_item(request_path: str, the_path: str, the_url: str, nav_item_content: str, nav_item_id: str = "") -> dict:
    context = dict(
        request_path=request_path, 
        the_path=the_path, 
        the_url=the_url, 
        nav_item_id=nav_item_id, 
        nav_item_content=nav_item_content, 
    )
    logger.info(f"category card context: {context}")
    return context
