from django import template
from app.dtos.destination_o import DestinationOQuerySet

register = template.Library()


@register.simple_tag
def filter_destinations(destinations: DestinationOQuerySet, category=None, continent=None):
    return destinations.filter(
        continent=continent, category=category
    )
