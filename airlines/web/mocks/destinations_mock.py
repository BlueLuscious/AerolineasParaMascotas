from web.dtos.destination_card_o import DestinationCardO
from web.dtos.destination_o import DestinationO


class DestinationMock:

    def mock_european_destinations(self) -> list["DestinationCardO"]:
        airports_static_path = "img/destination/airport"
        flags_static_path = "img/destination/flags"
        destinations: list[dict, str] = [
            {
                "destination": {
                    "name": "España",
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{flags_static_path}/spain-flag.png",
                    "airport_image": f"{airports_static_path}/spain-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-1 lg:col-end-3 lg:row-start-1 lg:translate-y-12 lg:hover:rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6",
                }
            },
            {
                "destination": {
                    "name": "Italia",
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{flags_static_path}/italy-flag.png",
                    "airport_image": f"{airports_static_path}/italy-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-2 lg:col-end-4 lg:row-start-2 lg:-translate-y-12 lg:hover:-rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6 lg:top-auto lg:-bottom-3 lg:-rotate-6",
                }
            },
            {
                "destination": {
                    "name": "Portugal",
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{flags_static_path}/portugal-flag.png",
                    "airport_image": f"{airports_static_path}/portugal-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-3 lg:col-end-5 lg:row-start-1 lg:translate-y-12 lg:hover:rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6",
                }
            },
            {
                "destination": {
                    "name": "Francia",
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{flags_static_path}/france-flag.png",
                    "airport_image": f"{airports_static_path}/france-airport.webp",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-4 lg:col-end-6 lg:row-start-2 lg:-translate-y-12 lg:hover:-rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6 lg:top-auto lg:-bottom-3 lg:-rotate-6",
                }
            },
            {
                "destination": {
                    "name": "Alemania",
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{flags_static_path}/germany-flag.png",
                    "airport_image": f"{airports_static_path}/germany-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-5 lg:col-end-7 lg:row-start-1 lg:translate-y-12 lg:hover:rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6",
                }
            },
            {
                "destination": {
                    "name": "Austria",
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{flags_static_path}/austria-flag.png",
                    "airport_image": f"{airports_static_path}/austria-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-6 lg:col-end-8 lg:row-start-2 lg:-translate-y-12 lg:hover:-rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6 lg:top-auto lg:-bottom-3 lg:-rotate-6",
                }
            },
        ]

        DestinationO._destinations = []
        DestinationCardO._destinations = []

        for item in destinations:
            DestinationCardO.create(
                country=DestinationO.create(**item.get("destination")),
                **item.get("destination_card")
            )
        return DestinationCardO.filter(continent="europa")


    def mock_american_destinations(self) -> list["DestinationCardO"]:
        airports_static_path = "img/destination/airport"
        flags_static_path = "img/destination/flags"
        destinations: list[dict, str] = [
            {
                "destination": {
                    "name": "Uruguay",
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{flags_static_path}/uruguay-flag.png",
                    "airport_image": f"{airports_static_path}/uruguay-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-1 lg:col-end-3 lg:row-start-1 lg:translate-y-12 lg:hover:rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6",
                }
            },
            {
                "destination": {
                    "name": "Chile",
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{flags_static_path}/chile-flag.png",
                    "airport_image": f"{airports_static_path}/chile-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-2 lg:col-end-4 lg:row-start-2 lg:-translate-y-12 lg:hover:-rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6 lg:top-auto lg:-bottom-3 lg:-rotate-6",
                }
            },
            {
                "destination": {
                    "name": "Bolivia",
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{flags_static_path}/bolivia-flag.png",
                    "airport_image": f"{airports_static_path}/bolivia-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-3 lg:col-end-5 lg:row-start-1 lg:translate-y-12 lg:hover:rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6",
                }
            },
            {
                "destination": {
                    "name": "Paraguay",
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{flags_static_path}/paraguay-flag.png",
                    "airport_image": f"{airports_static_path}/paraguay-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-4 lg:col-end-6 lg:row-start-2 lg:-translate-y-12 lg:hover:-rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6 lg:top-auto lg:-bottom-3 lg:-rotate-6",
                }
            },
            {
                "destination": {
                    "name": "Brasil",
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{flags_static_path}/brazil-flag.png",
                    "airport_image": f"{airports_static_path}/brazil-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-5 lg:col-end-7 lg:row-start-1 lg:translate-y-12 lg:hover:rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6",
                }
            },
            {
                "destination": {
                    "name": "Colombia",
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{flags_static_path}/colombia-flag.png",
                    "airport_image": f"{airports_static_path}/colombia-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-6 lg:col-end-8 lg:row-start-2 lg:-translate-y-12 lg:hover:-rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6 lg:top-auto lg:-bottom-3 lg:-rotate-6",
                }
            },
            {
                "destination": {
                    "name": "Perú",
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{flags_static_path}/peru-flag.png",
                    "airport_image": f"{airports_static_path}/peru-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-7 lg:col-end-9 lg:row-start-1 lg:translate-y-12 lg:hover:rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6",
                }
            },
        ]

        DestinationO._destinations = []
        DestinationCardO._destinations = []

        for item in destinations:
            DestinationCardO.create(
                country=DestinationO.create(**item.get("destination")),
                **item.get("destination_card")
            )
        return DestinationCardO.filter(continent="america")


    def mock_exotic_destinations(self) -> list["DestinationCardO"]:
        airports_static_path = "img/destination/airport"
        flags_static_path = "img/destination/flags"
        destinations: list[dict, str] = [
            {
                "destination": {
                    "name": "Australia",
                    "category": "Exotico",
                    "continent": "Oceania",
                    "flag_image": f"{flags_static_path}/australia-flag.png",
                    "airport_image": f"{airports_static_path}/australia-airport.webp",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-1 lg:col-end-3 lg:row-start-1 lg:translate-y-12 lg:hover:rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6",
                }
            },
            {
                "destination": {
                    "name": "Nueva Zelanda",
                    "category": "Exotico",
                    "continent": "Oceania",
                    "flag_image": f"{flags_static_path}/new-zealand-flag.png",
                    "airport_image": f"{airports_static_path}/new-zealand-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-2 lg:col-end-4 lg:row-start-2 lg:-translate-y-12 lg:hover:-rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6 lg:top-auto lg:-bottom-3 lg:-rotate-6",
                }
            },
            {
                "destination": {
                    "name": "Israel",
                    "category": "Exotico",
                    "continent": "Asia",
                    "flag_image": f"{flags_static_path}/israel-flag.png",
                    "airport_image": f"{airports_static_path}/israel-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-3 lg:col-end-5 lg:row-start-1 lg:translate-y-12 lg:hover:rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6",
                }
            },
            {
                "destination": {
                    "name": "Turquia",
                    "category": "Exotico",
                    "continent": "Asia",
                    "flag_image": f"{flags_static_path}/turkey-flag.png",
                    "airport_image": f"{airports_static_path}/turkey-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-4 lg:col-end-6 lg:row-start-2 lg:-translate-y-12 lg:hover:-rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6 lg:top-auto lg:-bottom-3 lg:-rotate-6",
                }
            },
            {
                "destination": {
                    "name": "Japon",
                    "category": "Exotico",
                    "continent": "Asia",
                    "flag_image": f"{flags_static_path}/japan-flag.png",
                    "airport_image": f"{airports_static_path}/japan-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-5 lg:col-end-7 lg:row-start-1 lg:translate-y-12 lg:hover:rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6",
                }
            },
            {
                "destination": {
                    "name": "China",
                    "category": "Exotico",
                    "continent": "Asia",
                    "flag_image": f"{flags_static_path}/china-flag.png",
                    "airport_image": f"{airports_static_path}/china-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-6 lg:col-end-8 lg:row-start-2 lg:-translate-y-12 lg:hover:-rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6 lg:top-auto lg:-bottom-3 lg:-rotate-6",
                }
            },
            {
                "destination": {
                    "name": "Corea del Sur",
                    "category": "Exotico",
                    "continent": "Asia",
                    "flag_image": f"{flags_static_path}/south-korea-flag.png",
                    "airport_image": f"{airports_static_path}/south-korea-airport.jpg",
                },
                "destination_card": {
                    "container_classes": "lg:col-start-7 lg:col-end-9 lg:row-start-1 lg:translate-y-12 lg:hover:rotate-1",
                    "classes": "card",
                    "label_classes": "-top-3 -right-3 rotate-6",
                }
            },
        ]

        DestinationO._destinations = []
        DestinationCardO._destinations = []

        for item in destinations:
            DestinationCardO.create(
                country=DestinationO.create(**item.get("destination")),
                **item.get("destination_card")
            )
        return DestinationCardO.filter(category="exotico")
