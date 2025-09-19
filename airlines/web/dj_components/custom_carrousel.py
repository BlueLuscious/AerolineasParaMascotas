from typing import NamedTuple
from django_components import Component, register


@register("CustomCarrousel")
class CustomCarrousel(Component):
    template_file = "components/atoms/custom-carrousel.html"

    class Kwargs(NamedTuple):
        id: str
        extra_classes: str = ""

    def get_template_data(self, args, kwargs: Kwargs, slots, context) -> dict:
        return dict(
            id=kwargs.id,
            extra_classes=kwargs.extra_classes,
        )
