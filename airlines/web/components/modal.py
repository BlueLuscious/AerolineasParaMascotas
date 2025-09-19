from django_unicorn.components import UnicornView
from app.dtos.destination_o import DestinationO


class ModalView(UnicornView):
    destination: dict = {}
    phone_map: str = "AEM"

    def select_destination(self, name: str = "") -> None:
        destination = DestinationO.filter(name=name).first()
        if destination:
            self.destination = destination.__dict__ if name != "" else {}
            if destination.continent.lower() == "norte america":
                self.phone_map = "VDR"
            else:
                if destination.name.lower() == "chile":
                    self.phone_map = "AEM"
                else:
                    self.phone_map = "AEM"
            