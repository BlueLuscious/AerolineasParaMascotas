def mock_faqs() -> list[dict[str, str]]:
    common_classes = "question flex items-center justify-between gap-x-2 w-full px-4 py-4 md:px-6 text-left group-hover:bg-secondary-grey_extralight"
    common_label_classes = "w-fit font-semibold"
    common_icon_classes = "size-6 transform transition-transform duration-300 ease-in-out"
    
    faqs: list[dict[str, str]] = [
        dict(
            id="question_1",
            question="¿Son una aerolínea?",
            answer="No, Aerolíneas para Mascotas es nuestro nombre ya que somos una empresa dedicada al exclusivamente al traslado aéreo y terrestre de mascotas, contamos con alianzas en Varios países para que trasladar a tu mascota no sea un impedimento, trabajando en forma conjunta logramos que tu mascota llegue a cualquier parte del mundo. Brindándote la mejor atención y seguridad que tu mascota merece.",
            classes=common_classes,
            label_classes=common_label_classes,
            icon_classes=common_icon_classes,
        ),
        dict(
            id="question_2",
            question="¿Qué peso debe tener mi mascota para viajar en cabina?",
            answer="Cada aerolínea cuenta con su propia reglamentación, en cuanto al peso y medida de la mascota, es por eso que recomendamos informarte previamente antes de realizar tu reserva aérea.",
            classes=common_classes,
            label_classes=common_label_classes,
            icon_classes=common_icon_classes,
        ),
        dict(
            id="question_3",
            question="¿Que documentación necesito para viajar con mi mascota en un vuelo internacional?",
            answer="La documentación necesaria para viajar con tu mascota en un vuelo internacional. Varía según el país de destino, es por eso que te aconsejamos que te contactes con nuestro equipo ya que son expertos en traslado de Mascotas y se encargan de gestionar toda la documentación necesaria para que vos puedas despreocuparte de esos trámites engorrosos.",
            classes=common_classes,
            label_classes=common_label_classes,
            icon_classes=common_icon_classes,
        ),
        dict(
            id="question_4",
            question="¿Qué tipos de Mascotas transladan?",
            answer="Trasladamos, tanto, caninos como felinos (Perros-Gatos) sin distinción de razas.",
            classes=common_classes,
            label_classes=common_label_classes,
            icon_classes=common_icon_classes,
        ),
        dict(
            id="question_5",
            question="¿Que aerolíneas trabajan con ustedes?",
            answer="Trabajamos con varias aerolíneas importantes para garantizar que tus mascotas lleguen al destino deseado, de manera segura y eficiente. Algunas de las aerolíneas con las que trabajamos son LATAM Airlines, Avianca entre otras.",
            classes=common_classes,
            label_classes=common_label_classes,
            icon_classes=common_icon_classes,
        ),
        dict(
            id="question_6",
            question="¿Que pasa si mi mascota posee necesidades especiales?",
            answer="Nuestro equipo de expertos en traslado de Mascotas está altamente capacitado para atender a Mascotas con necesidades especiales. Por favor, informarnos sobre cualquier prescripción médica u necesidad especial que presente tu mascota previamente para que podamos proporcionarle un cuidado adecuado y tomar los recaudos correspondientes.",
            classes=common_classes,
            label_classes=common_label_classes,
            icon_classes=common_icon_classes,
        ),
        dict(
            id="question_7",
            question="¿Cómo se garantiza la seguridad y el bienestar de mi mascota durante el traslado?",
            answer="Nuestra flota de vehículos están equipados para garantizar la seguridad y el confort de tu mascota, trabajamos con contenedores aprobados bajo norma IATA (Asociación Internacional de Transporte Aéreo). Nuestro equipo de expertos se encarga de atender a tus mascotas ante todo el proceso de traslado, brindando la atención necesaria.",
            classes=common_classes,
            label_classes=common_label_classes,
            icon_classes=common_icon_classes,
        ),
        dict(
            id="question_8",
            question="¿Si mascota viaja mediante un Vuelo de carga como es el proceso de embarque?",
            answer="Nuestro equipo de expertos se encarga de realizar todos los procedimientos protocolares desde el ingreso a la TCA (Terminal de Carga Aérea) hasta su embarque.Inicialmente realizando la colocación previa de todo lo necesario para su viaje, desde los paños absorbentes para sus necesidades, bebedero, comedero, hasta la colación de la ración de alimento extra en caso en que realice una escala aérea, cumpliendo con todos los requisitos indispensables para que tu mascota viaje segura.",
            classes=common_classes,
            label_classes=common_label_classes,
            icon_classes=common_icon_classes,
        ),
        dict(
            id="question_9",
            question="¿Si mi mascota es braquicefalo (Nariz Chata) qué precauciones, debo tomar?",
            answer="Al momento de viajar con tu mascota Braquicefalo debes tomar todos los recaudos necesarios previamente informándote sobre las políticas de la aerolínea con la que deseas viajar, siempre optando por un viaje seguro evitando el estrés y su exposición a las altas temperaturas, ya que son dos factores importantes a la hora de tomar un vuelo. Siempre se aconseja consultar con tu veterinario de confianza y elegir la  mejor opción según las necesidades de tu mascota. (A tener en cuenta: la época del año en el destino al que deseas viajar, se conseja que la temperatura no supere los 27° C° en toda la ruta Aérea).",
            classes=common_classes,
            label_classes=common_label_classes,
            icon_classes=common_icon_classes,
        ),
        dict(
            id="question_10",
            question="¿Cuentan con pensionado canino propio?",
            answer="No, solo contamos con pensionado transitorio para que las mascotas pasen en menor tiempo posible lejos de sus dueños, en este espacio le brindamos a tu mascota, la atención adecuada y el amor de un hogar, tal como en su casa. Con momentos de juegos, caricias, y paseos lo que hacen de esta corta estadía que no padezcan tristeza u estrés, siempre dependiendo de cada mascota. Por lo general nos quedamos a su cuidado nomás de 48 a 72 horas previas a su vuelo.",
            classes=common_classes,
            label_classes=common_label_classes,
            icon_classes=common_icon_classes,
        ),
        dict(
            id="question_11",
            question="¿Cual es el costo del servicio para trasladar a mi mascota?",
            answer="El costo del servicio de traslado de mascota, varía según la distancia, el tamaño y la raza entre otros factores. Te proporcionaremos un presupuesto en base a las características de tu mascota, el destino deseado y según la fecha en la que quieras realizar el mismo.",
            classes=common_classes,
            label_classes=common_label_classes,
            icon_classes=common_icon_classes,
        ),
        dict(
            id="question_12",
            question="¿Como realizo la reserva del servicio y el pago de la misma?",
            answer="Podes reservar nuestro servicio de traslado de Mascotas, a través de nuestro sitio web, o bien mediante nuestro canal de atención telefónica desde cualquier parte del mundo. El pago se puede realizar en Efectivo en nuestro domicilio o bien mediante transferencia bancaria a nuestras cuentas; para tu comodidad contamos con cuentas tanto en pesos como en dólares y euros, de esta manera podes realizar tu reserva de forma rápida y segura.",
            classes=common_classes,
            label_classes=common_label_classes,
            icon_classes=common_icon_classes,
        ),
    ]
    return faqs
