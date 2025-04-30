class DestinationO:
    _destinations: list["DestinationO"] = []

    def __init__(self, name: str, category: str, continent: str, flag_image: str, airport_image: str) -> None:
        self.name = name
        self.category = category
        self.continent = continent
        self.flag_image = flag_image
        self.airport_image = airport_image

    @classmethod
    def create(cls, **kwargs) -> "DestinationO":
        instance = cls(**kwargs)
        cls._destinations.append(instance)
        return instance

    @classmethod
    def all(cls) -> list["DestinationO"]:
        return cls._destinations
    
    @classmethod
    def filter(cls, category: str = None, continent: str = None) -> list["DestinationO"]:
        results = cls._destinations
        if category:
            results = [d for d in results if d.category.lower() == category.lower()]
        if continent:
            results = [d for d in results if d.continent.lower() == continent.lower()]
        return results
    