from django_unicorn.components import UnicornView
from app.dtos.destination_o import DestinationO


class ModalView(UnicornView):
    destination: dict = {}

    def select_destination(self, name: str = "") -> None:
        if name != self.destination.get("name"):
            self.destination = DestinationO.filter(name=name).first().__dict__ if name != "" else {}
            