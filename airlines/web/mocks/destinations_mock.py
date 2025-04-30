from web.dtos.destination_card_o import DestinationCardO
from web.dtos.destination_o import DestinationO


def mock_european_destinations() -> list["DestinationO"]:
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
                "container_classes": "lg:col-start-1 lg:col-end-3 lg:hover:rotate-1",
                "classes": "card",
                "label_classes": "-top-2 -right-2 rotate-12",
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
                "container_classes": "lg:col-start-2 lg:col-end-4 lg:translate-y-24 lg:hover:-rotate-1",
                "classes": "card",
                "label_classes": "-bottom-2 -right-2 -rotate-12",
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
                "container_classes": "lg:col-start-3 lg:col-end-5 lg:hover:rotate-1",
                "classes": "card",
                "label_classes": "-top-2 -right-2 rotate-12",
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
                "container_classes": "lg:col-start-4 lg:col-end-6 lg:translate-y-24 lg:hover:-rotate-1",
                "classes": "card",
                "label_classes": "-bottom-2 -right-2 -rotate-12",
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
                "container_classes": "lg:col-start-5 lg:col-end-7 lg:hover:rotate-1",
                "classes": "card",
                "label_classes": "-top-2 -right-2 rotate-12",
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
                "container_classes": "lg:col-start-6 lg:col-end-8 lg:translate-y-24 lg:hover:-rotate-1",
                "classes": "card",
                "label_classes": "-bottom-2 -right-2 -rotate-12",
            }
        },
    ]

    for item in destinations:
        DestinationCardO.create(
            country=DestinationO.create(**item.get("destination")),
            **item.get("destination_card")
        )

    return DestinationCardO.filter(continent="europa")
