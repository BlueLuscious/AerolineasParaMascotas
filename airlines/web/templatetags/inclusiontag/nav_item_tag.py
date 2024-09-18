import logging
from django import template

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("components/navbar-item.html")
def nav_item(request_path: str, the_path: str, the_url: str, nav_item_content: str) -> dict:
    logger.info(f"path: {the_path} | url: {the_url} | content: {nav_item_content}")
    context = {
        "request_path": request_path, 
        "the_path": the_path, 
        "the_url": the_url, 
        "nav_item_content": nav_item_content, 
    }
    logger.info(f"category card context: {context}")
    return context


@register.inclusion_tag("components/right-navbar-item.html")
def right_nav_item(request_path: str, the_path: str, the_url: str, nav_item_content: str) -> dict:
    logger.info(f"path: {the_path} | url: {the_url} | content: {nav_item_content}")
    context = {
        "request_path": request_path, 
        "the_path": the_path, 
        "the_url": the_url, 
        "nav_item_content": nav_item_content, 
    }
    logger.info(f"category card context: {context}")
    return context
