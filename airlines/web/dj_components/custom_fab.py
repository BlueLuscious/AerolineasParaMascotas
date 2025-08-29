from typing import NamedTuple
from django_components import Component, register


@register("CustomFab")
class CustomFab(Component):
    template_file = "components/atoms/custom-fab.html"

    class Kwargs(NamedTuple):
        id: str
        position: str = "bottom-3 right-3 sm:bottom-5 sm:right-5"
        colour: str = "gray-50"
        icon_name: str = "plus"
        extra_classes: str = ""
        icon_classes: str = ""
        dropdown_classes: str = ""

    def get_template_data(self, args, kwargs: Kwargs, slots, context) -> dict:
        return dict(
            id=kwargs.id,
            position=kwargs.position,
            colour=kwargs.colour,
            icon_name=kwargs.icon_name,
            extra_classes=kwargs.extra_classes,
            icon_classes=kwargs.icon_classes,
            dropdown_classes=kwargs.dropdown_classes,
        )
