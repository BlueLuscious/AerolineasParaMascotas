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
                    "name": "Uruguay",
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{self.flags_static_path}/uruguay-flag.png",
                    "airport_image": f"{self.airports_static_path}/uruguay-airport.jpg",
                    "airports": [],
                    "metadata": {
                        "description": [
                            {"no_key": [{"no_key": "Entrega en domicilio y de manera Terrestre desde Argentina. Gestionamos toda la documentación sanitaria."}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": "Chile",
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{self.flags_static_path}/chile-flag.png",
                    "airport_image": f"{self.airports_static_path}/chile-airport.jpg",
                    "airports": ["Aeropuerto Internacional Arturo Merino Benítez", ],
                    "metadata": {
                        "description": [
                            {"Documentación": [{"no_key": "Certificado sanitario, certificado de vacunación antirrábica y, en algunos casos, el Certificado Zoosanitario de Exportación."}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": "Bolivia",
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{self.flags_static_path}/bolivia-flag.png",
                    "airport_image": f"{self.airports_static_path}/bolivia-airport.jpg",
                    "airports": ["Aeropuerto Internacional Viru Viru (VVI)", ],
                    "metadata": {
                        "description": [
                            {"no_key": [{"no_key": "En Bolivia, los aeropuertos que permiten la entrada de mascotas generalmente son los aeropuertos internacionales, que incluyen La Paz (LPB), Santa Cruz (VVI) y Cochabamba (CBB). Sin embargo, es crucial verificar con la aerolínea y con el Ministerio de Desarrollo Rural y Tierras (MDRyT) los requisitos específicos para el transporte de mascotas, incluyendo la necesidad de un permiso de importación."}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": "Paraguay",
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{self.flags_static_path}/paraguay-flag.png",
                    "airport_image": f"{self.airports_static_path}/paraguay-airport.jpg",
                    "airports": ["Aeropuerto Internacional Silvio Pettirossi-Luque", ],
                    "metadata": {
                        "description": [
                            {"no_key": [{"no_key": "En Paraguay, los aeropuertos que permiten la entrada de mascotas generalmente están sujetos a los requisitos de la línea aérea y las regulaciones sanitarias del país. La mayoría de las líneas aéreas que operan en Paraguay, como Paranair, Flybondi, y Air Europa, permiten el transporte de mascotas en cabina o en bodega, siempre y cuando se cumplan ciertos requisitos, como el peso, las dimensiones del transportín, la edad de la mascota y la documentación necesaria."},]},
                            {"Documentación": [{"no_key": "Certificado de salud veterinario, carnet de vacunación (especialmente antirrábica), certificado de desparasitación y en algunos casos, pasaporte o certificado internacional."}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": "Brasil",
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{self.flags_static_path}/brazil-flag.png",
                    "airport_image": f"{self.airports_static_path}/brazil-airport.jpg",
                    "airports": [],
                    "metadata": {
                        "title": "Aeropuertos internacionales en Brasil que reciben mascotas" ,
                        "description": [
                            {"São Paulo (GRU)": [{"no_key": "Es el aeropuerto más grande de Brasil y ofrece múltiples conexiones internacionales, lo que lo convierte en una excelente opción para viajes con mascotas."}, ]},
                            {"Brasilia (BSB)": [{"no_key": "La capital de Brasil cuenta con servicios para viajeros con mascotas y ofrece una amplia gama de opciones para el transporte de animales."}, ]},
                            {"Belo Horizonte (CNF)": [{"no_key": "La región metropolitana de Belo Horizonte también cuenta con buena infraestructura para el transporte de animales en vuelos internacionales."}, ]},
                            {"Recife (REC)": [{"no_key": "Ubicado en el noreste de Brasil, Recife es otro aeropuerto popular que acepta mascotas en vuelos internacionales."}, ]},
                        ],
                    }
                },
            },
            {
                "destination": {
                    "name": "Colombia",
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{self.flags_static_path}/colombia-flag.png",
                    "airport_image": f"{self.airports_static_path}/colombia-airport.jpg",
                    "airports": ["Aeropuerto Internacional El Dorado (Bogotá)", "Aeropuerto internacional José María Córdova's (Medellín)", ],
                    "metadata": {
                        "title": "Ingreso a Colombia",
                        "description": [
                            {"no_key": [{"no_key": "Para ingresar al país con perros y gatos, se debe registrar previamente el ingreso a través del sitio web del ICA."}, ]},
                            {"no_key": [{"no_key": "Al llegar al aeropuerto, se deberá presentar la documentación requerida a la oficina del ICA para obtener el Certificado de Inspección Sanitaria (CIS)."}, ]},
                            {"no_key": [{"no_key": "Las mascotas deben tener vacunación vigente contra la rabia y estar desparasitadas."}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": "Perú",
                    "category": "Frecuente",
                    "continent": "America",
                    "flag_image": f"{self.flags_static_path}/peru-flag.png",
                    "airport_image": f"{self.airports_static_path}/peru-airport.jpg",
                    "airports": ["International Airport Jorge Chávez (Lima)", ],
                    "metadata": {
                        "title": "Requisitos para viajar con mascotas en el Aeropuerto Jorge Chávez",
                        "description": [
                            {"Certificado sanitario": [{"no_key": "Es indispensable para el ingreso a Perú, debe ser emitido en el país de origen y demostrar que la mascota está vacunada contra las enfermedades relevantes."}, ]},
                            {"Vacunas": [
                                    {"no_key": "Los animales deben estar vacunados contra las enfermedades específicas según su especie."}, 
                                    {"Perros": "Distemper, Hepatitis canina, Leptosirosis, Parvovirosis, Rabia, Parainfluenza."},
                                    {"Gatos": "Panleucoopenia felina, Calicivirosis, Rinotraqueitis, Leucemia felina, Rabia."}, 
                                ]
                            },
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": "Estados Unidos",
                    "category": "Frecuente",
                    "continent": "Norte America",
                    "flag_image": f"{self.flags_static_path}/usa-flag.png",
                    "airport_image": f"{self.airports_static_path}/usa-airport.jpg",
                    "airports": ["Aeropuerto internacional en Florida", ],
                    "metadata": {
                        "description": [
                            {"no_key": [{"no_key": "Para entrar con mascotas a Estados Unidos, es crucial seguir los requisitos de los Centers for Disease Control and Prevention (CDC). Los perros deben tener al menos 6 meses de edad, tener un microchip y estar vacunados contra la rabia. Además, deben tener un certificado de salud y de vacunación antirrábica válido. También se requiere un formulario de importación para perros, emitido por la CDC."}, ]},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": "Canadá",
                    "category": "Frecuente",
                    "continent": "Norte America",
                    "flag_image": f"{self.flags_static_path}/canada-flag.png",
                    "airport_image": f"{self.airports_static_path}/canada-airport.jpg",
                    "airports": ["Aeropuerto Internacional Pearson de Toronto (YYZ)", "Aeropuerto Internacional Montreal-Trudeau (YUL)", ],
                },
            },
            {
                "destination": {
                    "name": "Mexico",
                    "category": "Frecuente",
                    "continent": "Norte America",
                    "flag_image": f"{self.flags_static_path}/mexico-flag.png",
                    "airport_image": f"{self.airports_static_path}/mexico-airport.jpg",
                    "airports": ["Aeropuerto Internacional de la Ciudad de México (AICM)", ],
                    "metadata": {
                        "description": [
                            {"no_key": [{"no_key": "Para ingresar con mascotas, es importante consultar con la aerolínea sobre los requisitos específicos para cada tipo de mascota y el tamaño del contenedor."}, ]},
                            {"En resumen": [{"no_key": "El AICM es un aeropuerto pet-friendly, pero se deben cumplir con ciertos requisitos para viajar con mascotas, incluyendo el uso de contenedores/jaulas, el registro con la aerolínea y la consulta de los requisitos de SENASICA."}, ]},
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
            