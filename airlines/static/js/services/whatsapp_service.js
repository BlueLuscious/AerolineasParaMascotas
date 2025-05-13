export class WhatsappService {

    constructor() {
        this.phoneNumbers = {
            "AEM": "5491160375662",
            "VDR": "5491150599636",
            // 34663418545
        }
        this.messageWA = `Hola, completa con tus datos. Te atenderemos a la brevedad.

Nombre completo:
Correo Electronico:
Teléfono:`
    }

    redirectToWA(phone) {
        console.log(phone);
        window.location.href = `https://wa.me/${this.phoneNumbers[phone]}/?text=${encodeURIComponent(this.messageWA)}`;
    }

}
