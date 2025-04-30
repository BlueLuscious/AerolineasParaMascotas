from web.dtos.destination_o import DestinationO

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
    def all(cls) -> list["DestinationCardO"]:
        return cls._destinations
    
    @classmethod
    def filter(cls, category: str = None, continent: str = None) -> list["DestinationCardO"]:
        results = cls._destinations
        if category:
            results = [d for d in results if d.country.category.lower() == category.lower()]
        if continent:
            results = [d for d in results if d.country.continent.lower() == continent.lower()]
        return results
    