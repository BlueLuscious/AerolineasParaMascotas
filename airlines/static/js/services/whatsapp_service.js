export class WhatsappService {

    constructor() {
        this.phoneNumbers = [5491160375662, 34663418545]
        this.messageWA = `Hola, completa con tus datos. Te atenderemos a la brevedad.

        Nombre completo:
        Correo Electronico:
        Teléfono:`
    }

    redirectToWA(button, phone_index) {
        button.addEventListener('click', () => {
            window.location.href = `https://wa.me/${this.phoneNumbers[phone_index]}/?text=${encodeURIComponent(this.messageWA)}`
        })
    }

}
