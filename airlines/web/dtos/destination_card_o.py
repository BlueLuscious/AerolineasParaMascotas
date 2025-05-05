from app.utils.base_query_set import BaseQuerySet
from web.dtos.destination_o import DestinationO

class DestinationCardOQuerySet(BaseQuerySet["DestinationCardO"]):
    def filter(self, name:str=None, category:str=None, continent:str=None) -> list["DestinationCardO"]:
        result = self._data
        if name:
            result = [d for d in result if d.country.name.lower() == name.lower()]
        if category:
            result = [d for d in result if d.country.category.lower() == category.lower()]
        if continent:
            result = [d for d in result if d.country.continent.lower() == continent.lower()]
        return DestinationCardOQuerySet(result)


class DestinationCardO:
    _destinations: list["DestinationCardO"] = []

    def __init__(
        self,
        country: "DestinationO",
        container_classes: str,
        classes: str = "",
        label_classes: str = "",
    ):
        self.country = country
        self.container_classes = container_classes
        self.classes = classes
        self.label_classes = label_classes
        
    @classmethod
    def create(cls, **kwargs) -> "DestinationCardO":
        instance = cls(**kwargs)
        cls._destinations.append(instance)
        return instance

    @classmethod
    def all(cls) -> "DestinationCardOQuerySet":
        return DestinationCardOQuerySet(cls._destinations)
    