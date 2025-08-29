from django import template

register = template.Library()


@register.filter
def is_even(value: int) -> bool:
    return value % 2 == 0
