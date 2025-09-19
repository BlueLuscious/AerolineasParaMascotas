from django import template

register = template.Library()

@register.filter
def group_by(value: list, n: int) -> list[list]:
    """
    Divide una lista en grupos de n elementos.
    Ejemplo: [1,2,3,4,5] | group_by:2 => [[1,2],[3,4],[5]]
    """
    return [value[i:i+n] for i in range(0, len(value), n)]
