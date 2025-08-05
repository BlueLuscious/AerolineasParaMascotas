from django.utils.translation import gettext as _
from app.dtos.destination_o import DestinationO


class DestinationMock:

    def __init__(self) -> None:
        self.airports_static_path = "img/destination/airport"
        self.flags_static_path = "img/destination/flags"


    def mock_destinations(self) -> None:
        title_european_union = _("european_union_title")
        description_european_union = [
            {"no_key": [{"no_key": _("eu_description")}, ]},
            {_("documentation"): [
                    {_("pets_permits"): _("eu_description_doc_1")},
                    {_("vet_certificate_health"): _("eu_description_doc_2")},
                    {_("vaccination_certificate"): _("eu_description_doc_3")},
                ],
            },
            { _("vaccines_and_treatments"): [
                    {_("rabies_vaccine"): _("eu_description_health_1")},
                    {_("parasite_treatment"): _("eu_description_health_2")},
                ],
            },
            {_("identification"): [{_("microchip"): _("eu_description_microchip")}, ]},
            {_("permits_and_auth"): [
                    {_("import_permit"): _("eu_description_permits_1")},
                    {_("notification_authority"): _("eu_description_permits_2")},
                ],
            },
            {_("transport_conditions"): [
                    {_("transport_container"): _("eu_description_transport_1")},
                    {_("travel_conditions"): _("eu_description_transport_2")},
                ],
            },
            {_("important"): [
                    {_("check_specific_reqs"): _("eu_description_important_1")},
                    {_("consult_authority"): _("eu_description_important_2")},
                ],
            },
            {"Aerolineas para Mascotas": [
                    {"no_key": _("eu_description_aem")},
                ],
            },
        ]

        destinations: list[dict] = [
            {
                "destination": {
                    "name": _("spain"),
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{self.flags_static_path}/spain-flag.png",
                    "airport_image": f"{self.airports_static_path}/spain-airport.jpg",
                    "airports": ["Aeropuerto Adolfo Suárez Madrid-Barajas", ],
                    "metadata": {
                        "title": title_european_union,
                        "description": description_european_union,
                    },
                },
            },
            {
                "destination": {
                    "name": _("italy"),
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{self.flags_static_path}/italy-flag.png",
                    "airport_image": f"{self.airports_static_path}/italy-airport.jpg",
                    "airports": ["Aeropuerto de Roma-Fiumicino Metropolitan", ],
                    "metadata": {
                        "title": title_european_union,
                        "description": description_european_union,
                    },
                },
            },
            {
                "destination": {
                    "name": _("portugal"),
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{self.flags_static_path}/portugal-flag.png",
                    "airport_image": f"{self.airports_static_path}/portugal-airport.jpg",
                    "airports": ["Aeropuerto de Lisboa", "Aeropuerto de Oporto-Francisco Sá Carneiro", "Faro International Airport", ],
                    "metadata": {
                        "title": title_european_union,
                        "description": description_european_union,
                    },
                },
            },
            {
                "destination": {
                    "name": _("france"),
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{self.flags_static_path}/france-flag.png",
                    "airport_image": f"{self.airports_static_path}/france-airport.webp",
                    "airports": ["Aeropuerto de París-Charles de Gaulle", ],
                    "metadata": {
                        "title": title_european_union,
                        "description": description_european_union,
                    },
                },
            },
            {
                "destination": {
                    "name": _("germany"),
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{self.flags_static_path}/germany-flag.png",
                    "airport_image": f"{self.airports_static_path}/germany-airport.jpg",
                    "airports": ["Aeropuerto de Frankfurt (FRA)", ],
                    "metadata": {
                        "title": title_european_union,
                        "description": description_european_union,
                    },
                },
            },
            {
                "destination": {
                    "name": _("austria"),
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{self.flags_static_path}/austria-flag.png",
                    "airport_image": f"{self.airports_static_path}/austria-airport.jpg",
                    "airports": ["Aeropuerto de Viena-Schwechat", ],
                    "metadata": {
                        "title": title_european_union,
                        "description": description_european_union,
                    },
                },
            },
            {
                "destination": {
                    "name": _("uruguay"),
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{self.flags_static_path}/uruguay-flag.png",
                    "airport_image": f"{self.airports_static_path}/uruguay-airport.jpg",
                    "airports": [],
                    "metadata": {
                        "description": [
                            {"no_key": [{"no_key": _("uruguay_description")}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": _("chile"),
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{self.flags_static_path}/chile-flag.png",
                    "airport_image": f"{self.airports_static_path}/chile-airport.jpg",
                    "airports": ["Aeropuerto Internacional Arturo Merino Benítez", ],
                    "metadata": {
                        "description": [
                            {_("documentation"): [{"no_key": _("chile_description_doc")}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": _("bolivia"),
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{self.flags_static_path}/bolivia-flag.png",
                    "airport_image": f"{self.airports_static_path}/bolivia-airport.jpg",
                    "airports": ["Aeropuerto Internacional Viru Viru (VVI)", ],
                    "metadata": {
                        "description": [
                            {"no_key": [{"no_key": _("bolivia_description")}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": _("paraguay"),
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{self.flags_static_path}/paraguay-flag.png",
                    "airport_image": f"{self.airports_static_path}/paraguay-airport.jpg",
                    "airports": ["Aeropuerto Internacional Silvio Pettirossi-Luque", ],
                    "metadata": {
                        "description": [
                            {"no_key": [{"no_key": _("paraguay_description")},]},
                            {_("documentation"): [{"no_key": _("paraguay_description_doc")}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": _("brazil"),
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{self.flags_static_path}/brazil-flag.png",
                    "airport_image": f"{self.airports_static_path}/brazil-airport.jpg",
                    "airports": [],
                    "metadata": {
                        "title": _("brazil_title") ,
                        "description": [
                            {"São Paulo (GRU)": [{"no_key": _("brazil_description_airport_1")}, ]},
                            {"Brasilia (BSB)": [{"no_key": _("brazil_description_airport_2")}, ]},
                            {"Belo Horizonte (CNF)": [{"no_key": _("brazil_description_airport_3")}, ]},
                            {"Recife (REC)": [{"no_key": _("brazil_description_airport_4")}, ]},
                        ],
                    }
                },
            },
            {
                "destination": {
                    "name": _("colombia"),
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{self.flags_static_path}/colombia-flag.png",
                    "airport_image": f"{self.airports_static_path}/colombia-airport.jpg",
                    "airports": ["Aeropuerto Internacional El Dorado (Bogotá)", "Aeropuerto internacional José María Córdova's (Medellín)", ],
                    "metadata": {
                        "title": _("colombia_title"),
                        "description": [
                            {"no_key": [{"no_key": _("colombia_description_1")}, ]},
                            {"no_key": [{"no_key": _("colombia_description_2")}, ]},
                            {"no_key": [{"no_key": _("colombia_description_3")}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": _("peru"),
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{self.flags_static_path}/peru-flag.png",
                    "airport_image": f"{self.airports_static_path}/peru-airport.jpg",
                    "airports": ["International Airport Jorge Chávez (Lima)", ],
                    "metadata": {
                        "title": _("peru_title"),
                        "description": [
                            {_("health_certificate"): [{"no_key": _("peru_description_health_certificate")}, ]},
                            {_("vaccines"): [
                                    {"no_key": _("peru_description_vaccines")}, 
                                    {_("dogs"): _("peru_description_vaccines_dogs")},
                                    {_("cats"): _("peru_description_vaccines_cats")}, 
                                ]
                            },
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": _("usa"),
                    "category": "Frecuente",
                    "continent": "Norte America",
                    "flag_image": f"{self.flags_static_path}/usa-flag.png",
                    "airport_image": f"{self.airports_static_path}/usa-airport.jpg",
                    "airports": ["Aeropuerto internacional en Florida", ],
                    "metadata": {
                        "description": [
                            {"no_key": [{"no_key": _("usa_description")}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": _("canada"),
                    "category": "Frecuente",
                    "continent": "Norte America",
                    "flag_image": f"{self.flags_static_path}/canada-flag.png",
                    "airport_image": f"{self.airports_static_path}/canada-airport.jpg",
                    "airports": ["Aeropuerto Internacional Pearson de Toronto (YYZ)", "Aeropuerto Internacional Montreal-Trudeau (YUL)", ],
                    "metadata": {
                        "description": [
                            {"no_key": [{"no_key": _("canada_description")}, ]},
                            {_("general_reqs_for_dogs_and_cats"): [
                                    {_("rabies_vaccine"): _("canada_description_vaccines")}, 
                                    {_("vet_certificate_health_international"): _("canada_description_health_international")}, 
                                    {_("vet_certificate_health"): _("canada_description_health")}, 
                                ],
                            },
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": _("mexico"),
                    "category": "Frecuente",
                    "continent": "Norte America",
                    "flag_image": f"{self.flags_static_path}/mexico-flag.png",
                    "airport_image": f"{self.airports_static_path}/mexico-airport.jpg",
                    "airports": ["Aeropuerto Internacional de la Ciudad de México (AICM)", ],
                    "metadata": {
                        "description": [
                            {"no_key": [{"no_key": _("mexico_description")}, ]},
                            {_("in_summary"): [{"no_key": _("mexico_description_summary")}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": _("australia"),
                    "category": "Exotico",
                    "continent": "Oceania",
                    "flag_image": f"{self.flags_static_path}/australia-flag.png",
                    "airport_image": f"{self.airports_static_path}/australia-airport.webp",
                    "airports": ["Aeropuerto Internacional de Melbourne", ],
                    "metadata": {
                        "description": [
                            {_("quarantine"): [{"no_key": _("australia_description_quarantine")}, ]},
                            {_("cargo_hold_trip"): [{"no_key": _("australia_description_cargo_hold")}, ]},
                            {_("no_national_transfers"): [{"no_key": _("australia_description_national_transfers")}, ]},
                            {_("quarantine_reqs"): [{"no_key": _("australia_description_quarantine_reqs")}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": _("new_zealand"),
                    "category": "Exotico",
                    "continent": "Oceania",
                    "flag_image": f"{self.flags_static_path}/new-zealand-flag.png",
                    "airport_image": f"{self.airports_static_path}/new-zealand-airport.jpg",
                    "airports": ["Aeropuerto de Auckland", "Aeropuerto de Christchurc", ],
                    "metadata": {
                        "description": [
                            {"no_key": [{"no_key": _("new_zealand_description_1")}, ]},
                            {"no_key": [{"no_key": _("new_zealand_description_2")}, ]},
                            {"no_key": [{"no_key": _("new_zealand_description_3")}, ]},
                            {"no_key": [{"no_key": _("new_zealand_description_4")}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": _("israel"),
                    "category": "Exotico",
                    "continent": "Asia",
                    "flag_image": f"{self.flags_static_path}/israel-flag.png",
                    "airport_image": f"{self.airports_static_path}/israel-airport.jpg",
                    "airports": ["Aeropuerto Internacional Ben Gurión en Lod", ],
                    "metadata": {
                        "description": [
                            {"no_key": [{"no_key": _("israel_description")}, ]},
                            {_("pets_in_cabin"): [{"no_key": _("israel_description_cabin")}, ]},
                            {_("pets_in_hold"): [{"no_key": _("israel_description_hold")}, ]},
                            {_("import_permit"): [{"no_key": _("israel_description_import_license")}, ]},
                            {_("others_considerations"): [{"no_key": _("israel_description_other")}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": _("turkey"),
                    "category": "Exotico",
                    "continent": "Asia",
                    "flag_image": f"{self.flags_static_path}/turkey-flag.png",
                    "airport_image": f"{self.airports_static_path}/turkey-airport.jpg",
                    "airports": ["Aeropuerto Internacional de Estambul (IST)", ],
                    "metadata": {
                        "description": [
                            {"no_key": [{"no_key": _("turkey_description")}, ]},
                            {"Turkish Airlines": [{"no_key": _("turkey_description_airlines")}, ]},
                            {_("considerations"): [{"no_key": _("turkey_description_other")}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": _("japan"),
                    "category": "Exotico",
                    "continent": "Asia",
                    "flag_image": f"{self.flags_static_path}/japan-flag.png",
                    "airport_image": f"{self.airports_static_path}/japan-airport.jpg",
                    "airports": ["Aeropuerto de Haneda (HND)", "Aeropuerto de Narita (NRT)", ],
                    "metadata": {
                        "title": _("japan_title"),
                        "description": [
                            {_("microchip"): [{"no_key": _("japan_description_microchip")}, ]},
                            {_("rabies_vaccine"): [{"no_key": _("japan_description_vaccines")}, ]},
                            {_("rabies_titer_test"): [{"no_key": _("japan_description_rage")}, ]},
                            {_("quarantine"): [{"no_key": _("japan_description_quarantine")}, ]},
                            {_("documentation"): [{"no_key": _("japan_description_doc")}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": _("china"),
                    "category": "Exotico",
                    "continent": "Asia",
                    "flag_image": f"{self.flags_static_path}/china-flag.png",
                    "airport_image": f"{self.airports_static_path}/china-airport.jpg",
                    "airports": ["Aeropuerto Internacional de Beijing", ],
                    "metadata": {
                        "description": [
                            {_("quarantine"): [{"no_key": _("china_description_quarantine")}, ]},
                            {_("restrictions"): [{"no_key": _("china_description_restrictions")}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": _("south_korea"),
                    "category": "Exotico",
                    "continent": "Asia",
                    "flag_image": f"{self.flags_static_path}/south-korea-flag.png",
                    "airport_image": f"{self.airports_static_path}/south-korea-airport.jpg",
                    "airports": ["Aeropuerto Internacional de Incheon (Seúl)", ],
                    "metadata": {
                        "title": _("south_korea_title"),
                        "description": [
                            {_("documentation"): [{"no_key": _("south_korea_description_doc")}, ]},
                            {_("transport_conditions"): [{"no_key": _("south_korea_description_transport")}, ]},
                        ],
                    },
                },
            },
        ]

        DestinationO._destinations = []

        for item in destinations:
            DestinationO.create(**item.get("destination"))
            