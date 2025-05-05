from django import template
from web.dtos.destination_card_o import DestinationCardOQuerySet

register = template.Library()


@register.simple_tag
def filter_destinations(destinations: DestinationCardOQuerySet, category=None, continent=None):
    return destinations.filter(
        continent=continent, category=category
    )
