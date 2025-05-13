from django_unicorn.components import UnicornView
from app.dtos.destination_o import DestinationO


class ModalView(UnicornView):
    destination: dict = {}
    phone_map: str = "AEM"

    def select_destination(self, name: str = "") -> None:
        destination = DestinationO.filter(name=name).first()
        if destination:
            self.destination = destination.__dict__ if name != "" else {}
            self.phone_map = "VDR" if destination.continent.lower() == "norte america" else "AEM"
            