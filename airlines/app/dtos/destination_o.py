from app.utils.base_query_set import BaseQuerySet

class DestinationOQuerySet(BaseQuerySet["DestinationO"]):
    def filter(self, name:str=None, category:str=None, continent:str=None) -> "DestinationOQuerySet":
        result = self._data
        if name:
            result = [d for d in result if d.name.lower() == name.lower()]
        if category:
            result = [d for d in result if d.category.lower() == category.lower()]
        if continent:
            result = [d for d in result if d.continent.lower() == continent.lower()]
        return DestinationOQuerySet(result)


class DestinationO:
    _destinations: list["DestinationO"] = []

    def __init__(
        self, name:str, category:str, continent:str, airports:list=[], flag_image:str="", airport_image:str="", metadata:dict[str, dict]={}
    ) -> None:
        self.name = name
        self.category = category
        self.continent = continent
        self.airports = airports
        self.flag_image = flag_image
        self.airport_image = airport_image
        self.metadata = metadata

    @classmethod
    def create(cls, **kwargs) -> "DestinationO":
        instance = cls(**kwargs)
        cls._destinations.append(instance)
        return instance

    @classmethod
    def all(cls) -> "DestinationOQuerySet":
        return DestinationOQuerySet(cls._destinations)
    
    @classmethod
    def filter(cls, name:str=None, category:str=None, continent:str=None) -> "DestinationOQuerySet":
        return DestinationOQuerySet(cls._destinations).filter(name, category, continent)
    