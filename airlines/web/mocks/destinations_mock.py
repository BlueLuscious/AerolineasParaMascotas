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
                    # metadata
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
                    "name": "Australia",
                    "category": "Exotico",
                    "continent": "Oceania",
                    "flag_image": f"{self.flags_static_path}/australia-flag.png",
                    "airport_image": f"{self.airports_static_path}/australia-airport.webp",
                    "airports": ["Aeropuerto Internacional de Melbourne", ],
                    "metadata": {
                        "description": [
                            {"Cuarentena": [{"no_key": "Una vez que la mascota llega a Melbourne, será trasladada al centro de cuarentena posterior a la entrada en Mickleham para un período de cuarentena, que varía según el país de origen de la mascota. Desde Argentina la cuarentena no supera los 30 días."}, ]},
                            {"Viaje de bodega de carga": [{"no_key": "Las mascotas deben viajar en la bodega de carga como carga declarada en un transportín aprobado por la IATA."}, ]},
                            {"No se permiten traslados nacionales": [{"no_key": "No se permite que las mascotas lleguen a otro aeropuerto australiano y luego viajen en un vuelo nacional a Melbourne."}, ]},
                            {"Requisitos de cuarentena": [{"no_key": "Se deben seguir los requisitos de cuarentena estrictos del Departamento de Agricultura, Pesca y Recursos Forestales (DAFF) de Australia"}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": "Nueva Zelanda",
                    "category": "Exotico",
                    "continent": "Oceania",
                    "flag_image": f"{self.flags_static_path}/new-zealand-flag.png",
                    "airport_image": f"{self.airports_static_path}/new-zealand-airport.jpg",
                    "airports": ["Aeropuerto de Auckland", "Aeropuerto de Christchurc", ],
                    "metadata": {
                        "description": [
                            {"no_key": [{"no_key": "Para traer mascotas a Nueva Zelanda, es fundamental que se cumplan los estrictos requisitos sanitarios y veterinarios del país."}, ]},
                            {"no_key": [{"no_key": "El Ministerio de Industrias Primarias (MPI) solo permite la entrada de perros y gatos de países considerados libres o controlados de rabia."}, ]},
                            {"no_key": [{"no_key": "Las mascotas deben tener un microchip antes de cualquier tratamiento para la importación."}, ]},
                            {"no_key": [{"no_key": "Se necesita documentación que confirme que el microchip fue implantado y/o escaneado antes de la vacunación primaria contra la rabia y todos los tratamientos posteriores."}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": "Israel",
                    "category": "Exotico",
                    "continent": "Asia",
                    "flag_image": f"{self.flags_static_path}/israel-flag.png",
                    "airport_image": f"{self.airports_static_path}/israel-airport.jpg",
                    "airports": ["Aeropuerto Internacional Ben Gurión en Lod", ],
                    "metadata": {
                        "description": [
                            {"no_key": [{"no_key": "El Aeropuerto Internacional Ben Gurión en Lod, cerca de Tel Aviv, es el principal aeropuerto internacional de Israel y permite la entrada de mascotas."}, ]},
                            {"Mascotas en cabina": [{"no_key": "Las mascotas pueden viajar en cabina si pesan hasta 8 kg, incluyendo el transportín, y si el transportín cumple con las dimensiones permitidas por la aerolínea."}, ]},
                            {"Mascotas en bodega": [{"no_key": "Las mascotas también pueden viajar como equipaje en bodega, pero deben estar en una jaula rígida y segura, según las regulaciones de la aerolínea."}, ]},
                            {"Permiso de importación": [{"no_key": "Es crucial obtener el permiso de importación antes de viajar a Israel con mascotas."}, ]},
                            {"Otras consideraciones": [{"no_key": "Es recomendable verificar las regulaciones específicas de cada aerolínea antes de reservar el vuelo, ya que pueden variar."}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": "Turquía",
                    "category": "Exotico",
                    "continent": "Asia",
                    "flag_image": f"{self.flags_static_path}/turkey-flag.png",
                    "airport_image": f"{self.airports_static_path}/turkey-airport.jpg",
                    "airports": ["Aeropuerto Internacional de Estambul (IST)", ],
                    "metadata": {
                        "description": [
                            {"no_key": [{"no_key": "Además, algunas aerolíneas, como Turkish Airlines, tienen políticas específicas para el transporte de mascotas."}, ]},
                            {"Turkish Airlines": [{"no_key": "Tiene una política de mascotas que incluye la posibilidad de viajar en cabina o bodega, según el peso y tamaño de la mascota y su transportín."}, ]},
                            {"Consideraciones": [{"no_key": "Es importante verificar las políticas de cada aerolínea y cumplir con los requisitos de salud y documentación necesarios para viajar con mascotas a Turquía."}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": "Japón",
                    "category": "Exotico",
                    "continent": "Asia",
                    "flag_image": f"{self.flags_static_path}/japan-flag.png",
                    "airport_image": f"{self.airports_static_path}/japan-airport.jpg",
                    "airports": ["Aeropuerto de Haneda (HND)", "Aeropuerto de Narita (NRT)", ],
                    "metadata": {
                        "title": "Requisitos para viajar con mascotas a Japón",
                        "description": [
                            {"Microchip": [{"no_key": "Las mascotas deben tener un microchip."}, ]},
                            {"Vacunación contra la rabia": [{"no_key": "La vacunación debe ser al menos 30 días antes de la entrada al país."}, ]},
                            {"Prueba de titulación de rabia": [{"no_key": "Se requiere una prueba para asegurar la efectividad de la vacuna contra la rabia."}, ]},
                            {"Cuarentena": [{"no_key": "Dependiendo de los requisitos cumplidos por la mascota, puede haber un período de cuarentena de 12 horas o más."}, ]},
                            {"Documentación": [{"no_key": "Se debe presentar la documentación requerida, como el certificado ASE-3293 y la solicitud de inspección de importación."}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": "China",
                    "category": "Exotico",
                    "continent": "Asia",
                    "flag_image": f"{self.flags_static_path}/china-flag.png",
                    "airport_image": f"{self.airports_static_path}/china-airport.jpg",
                    "airports": ["Aeropuerto Internacional de Beijing", ],
                    "metadata": {
                        "description": [
                            {"Cuarentena": [{"no_key": "Las mascotas que ingresan a China pueden estar sujetas a cuarentena."}, ]},
                            {"Restricciones": [{"no_key": "Solo se permite una mascota por pasajero."}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": "Corea del Sur",
                    "category": "Exotico",
                    "continent": "Asia",
                    "flag_image": f"{self.flags_static_path}/south-korea-flag.png",
                    "airport_image": f"{self.airports_static_path}/south-korea-airport.jpg",
                    "airports": ["Aeropuerto Internacional de Incheon (Seúl)", ],
                    "metadata": {
                        "title": "Requisitos para viajar con mascotas a Corea del Sur",
                        "description": [
                            {"Documentación": [{"no_key": "Es necesario tener la documentación de la mascota en regla, incluyendo el certificado de vacunación contra la rabia y otros requisitos que pueden variar según el país de origen de la mascota. Desde Argentina exigen test de anticuerpos de rabia."}, ]},
                            {"Condiciones de transporte": [{"no_key": "Las aerolíneas tienen sus propias políticas sobre el transporte de mascotas, por lo que es importante consultar con la aerolínea antes de viajar."}, ]},
                        ],
                    },
                },
            },
        ]

        DestinationO._destinations = []

        for item in destinations:
            DestinationO.create(**item.get("destination"))
            