from app.dtos.destination_o import DestinationO


class DestinationMock:

    def __init__(self) -> None:
        self.airports_static_path = "img/destination/airport"
        self.flags_static_path = "img/destination/flags"


    def mock_destinations(self) -> None:
        destinations: list[dict] = [
            {
                "destination": {
                    "name": "España",
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{self.flags_static_path}/spain-flag.png",
                    "airport_image": f"{self.airports_static_path}/spain-airport.jpg",
                    "airports": ["Aeropuerto Adolfo Suárez Madrid-Barajas", ],
                },
            },
            {
                "destination": {
                    "name": "Italia",
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{self.flags_static_path}/italy-flag.png",
                    "airport_image": f"{self.airports_static_path}/italy-airport.jpg",
                    "airports": ["Aeropuerto de Roma-Fiumicino Metropolitan", ],
                },
            },
            {
                "destination": {
                    "name": "Portugal",
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{self.flags_static_path}/portugal-flag.png",
                    "airport_image": f"{self.airports_static_path}/portugal-airport.jpg",
                    "airports": ["Aeropuerto de Lisboa", "Aeropuerto de Oporto-Francisco Sá Carneiro", "Faro International Airport", ],
                },
            },
            {
                "destination": {
                    "name": "Francia",
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{self.flags_static_path}/france-flag.png",
                    "airport_image": f"{self.airports_static_path}/france-airport.webp",
                    "airports": ["Aeropuerto de París-Charles de Gaulle", ],
                },
            },
            {
                "destination": {
                    "name": "Alemania",
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{self.flags_static_path}/germany-flag.png",
                    "airport_image": f"{self.airports_static_path}/germany-airport.jpg",
                    "airports": ["Aeropuerto de Frankfurt (FRA)", ],
                },
            },
            {
                "destination": {
                    "name": "Austria",
                    "category": "Frecuente",
                    "continent": "Europa",
                    "flag_image": f"{self.flags_static_path}/austria-flag.png",
                    "airport_image": f"{self.airports_static_path}/austria-airport.jpg",
                    "airports": ["Aeropuerto de Viena-Schwechat", ],
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
                            {"no_key": "Entrega en domicilio y de manera Terrestre desde Argentina. Gestionamos toda la documentación sanitaria."},
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
                            {"Documentación": "Certificado sanitario, certificado de vacunación antirrábica y, en algunos casos, el Certificado Zoosanitario de Exportación."},
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
                            {"no_key": "En Bolivia, los aeropuertos que permiten la entrada de mascotas generalmente son los aeropuertos internacionales, que incluyen La Paz (LPB), Santa Cruz (VVI) y Cochabamba (CBB). Sin embargo, es crucial verificar con la aerolínea y con el Ministerio de Desarrollo Rural y Tierras (MDRyT) los requisitos específicos para el transporte de mascotas, incluyendo la necesidad de un permiso de importación."},
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
                            {"no_key": "En Paraguay, los aeropuertos que permiten la entrada de mascotas generalmente están sujetos a los requisitos de la línea aérea y las regulaciones sanitarias del país. La mayoría de las líneas aéreas que operan en Paraguay, como Paranair, Flybondi, y Air Europa, permiten el transporte de mascotas en cabina o en bodega, siempre y cuando se cumplan ciertos requisitos, como el peso, las dimensiones del transportín, la edad de la mascota y la documentación necesaria."},
                            {"Documentación": "Certificado de salud veterinario, carnet de vacunación (especialmente antirrábica), certificado de desparasitación y en algunos casos, pasaporte o certificado internacional."}
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
                    "airports": ["São Paulo (GRU)", "Río de Janeiro (GIG)", "Brasilia (BSB)", "Belo Horizonte (CNF)", "Recife (REC)", ],
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
                            {"no_key": "Para ingresar al país con perros y gatos, se debe registrar previamente el ingreso a través del sitio web del ICA."},
                            {"no_key": "Al llegar al aeropuerto, se deberá presentar la documentación requerida a la oficina del ICA para obtener el Certificado de Inspección Sanitaria (CIS)."},
                            {"no_key": "Las mascotas deben tener vacunación vigente contra la rabia y estar desparasitadas."},
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
                            {"Certificado sanitario": "Es indispensable para el ingreso a Perú, debe ser emitido en el país de origen y demostrar que la mascota está vacunada contra las enfermedades relevantes."},
                            {"Vacunas": "Los animales deben estar vacunados contra las enfermedades específicas según su especie (Perros: Distemper, Hepatitis canina, Leptosirosis, Parvovirosis, Rabia, Parainfluenza; Gatos: Panleucoopenia felina, Calicivirosis, Rinotraqueitis, Leucemia felina, Rabia"},
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
                    "airports": [],
                },
            },
            {
                "destination": {
                    "name": "Canada",
                    "category": "Frecuente",
                    "continent": "Norte America",
                    "flag_image": f"{self.flags_static_path}/canada-flag.png",
                    "airport_image": f"{self.airports_static_path}/canada-airport.jpg",
                    "airports": [],
                },
            },
            {
                "destination": {
                    "name": "Mexico",
                    "category": "Frecuente",
                    "continent": "Norte America",
                    "flag_image": f"{self.flags_static_path}/mexico-flag.png",
                    "airport_image": f"{self.airports_static_path}/mexico-airport.jpg",
                    "airports": [],
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
                            {"Cuarentena": "Una vez que la mascota llega a Melbourne, será trasladada al centro de cuarentena posterior a la entrada en Mickleham para un período de cuarentena, que varía según el país de origen de la mascota. Desde Argentina la cuarentena no supera los 30 días."},
                            {"Viaje de bodega de carga": "Las mascotas deben viajar en la bodega de carga como carga declarada en un transportín aprobado por la IATA."},
                            {"No se permiten traslados nacionales": "No se permite que las mascotas lleguen a otro aeropuerto australiano y luego viajen en un vuelo nacional a Melbourne."},
                            {"Requisitos de cuarentena": "Se deben seguir los requisitos de cuarentena estrictos del Departamento de Agricultura, Pesca y Recursos Forestales (DAFF) de Australia"},
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
                            {"no_key": "Para traer mascotas a Nueva Zelanda, es fundamental que se cumplan los estrictos requisitos sanitarios y veterinarios del país."},
                            {"no_key": "El Ministerio de Industrias Primarias (MPI) solo permite la entrada de perros y gatos de países considerados libres o controlados de rabia."},
                            {"no_key": "Las mascotas deben tener un microchip antes de cualquier tratamiento para la importación."},
                            {"no_key": "Se necesita documentación que confirme que el microchip fue implantado y/o escaneado antes de la vacunación primaria contra la rabia y todos los tratamientos posteriores."},
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
                            {"no_key": "El Aeropuerto Internacional Ben Gurión en Lod, cerca de Tel Aviv, es el principal aeropuerto internacional de Israel y permite la entrada de mascotas."},
                            {"Mascotas en cabina": "Las mascotas pueden viajar en cabina si pesan hasta 8 kg, incluyendo el transportín, y si el transportín cumple con las dimensiones permitidas por la aerolínea."},
                            {"Mascotas en bodega": "Las mascotas también pueden viajar como equipaje en bodega, pero deben estar en una jaula rígida y segura, según las regulaciones de la aerolínea."},
                            {"Permiso de importación": "Es crucial obtener el permiso de importación antes de viajar a Israel con mascotas."},
                            {"Otras consideraciones": "Es recomendable verificar las regulaciones específicas de cada aerolínea antes de reservar el vuelo, ya que pueden variar."},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": "Turquia",
                    "category": "Exotico",
                    "continent": "Asia",
                    "flag_image": f"{self.flags_static_path}/turkey-flag.png",
                    "airport_image": f"{self.airports_static_path}/turkey-airport.jpg",
                    "airports": ["Aeropuerto Internacional de Estambul (IST)", ],
                    "metadata": {
                        "description": [
                            {"no_key": "Además, algunas aerolíneas, como Turkish Airlines, tienen políticas específicas para el transporte de mascotas."},
                            {"Turkish Airlines": "Tiene una política de mascotas que incluye la posibilidad de viajar en cabina o bodega, según el peso y tamaño de la mascota y su transportín."},
                            {"Consideraciones": "Es importante verificar las políticas de cada aerolínea y cumplir con los requisitos de salud y documentación necesarios para viajar con mascotas a Turquía."},
                        ],
                    },
                },
            },
            {
                "destination": {
                    "name": "Japon",
                    "category": "Exotico",
                    "continent": "Asia",
                    "flag_image": f"{self.flags_static_path}/japan-flag.png",
                    "airport_image": f"{self.airports_static_path}/japan-airport.jpg",
                    "airports": ["Aeropuerto de Haneda (HND)", "Aeropuerto de Narita (NRT)", ],
                    "metadata": {
                        "title": "Requisitos para viajar con mascotas a Japón",
                        "description": [
                            {"Microchip": "Las mascotas deben tener un microchip."},
                            {"Vacunación contra la rabia": "La vacunación debe ser al menos 30 días antes de la entrada al país."},
                            {"Prueba de titulación de rabia": "Se requiere una prueba para asegurar la efectividad de la vacuna contra la rabia."},
                            {"Cuarentena": "Dependiendo de los requisitos cumplidos por la mascota, puede haber un período de cuarentena de 12 horas o más."},
                            {"Documentación": "Se debe presentar la documentación requerida, como el certificado ASE-3293 y la solicitud de inspección de importación."},
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
                            {"Cuarentena": "Las mascotas que ingresan a China pueden estar sujetas a cuarentena."},
                            {"Restricciones": "Solo se permite una mascota por pasajero."},
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
                            {"Documentación": "Es necesario tener la documentación de la mascota en regla, incluyendo el certificado de vacunación contra la rabia y otros requisitos que pueden variar según el país de origen de la mascota. Desde Argentina exigen test de anticuerpos de rabia."},
                            {"Condiciones de transporte": "Las aerolíneas tienen sus propias políticas sobre el transporte de mascotas, por lo que es importante consultar con la aerolínea antes de viajar."},
                        ],
                    },
                },
            },
        ]

        DestinationO._destinations = []

        for item in destinations:
            DestinationO.create(**item.get("destination"))
            