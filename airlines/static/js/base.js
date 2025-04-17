import { WhatsappService } from "./services/whatsapp_service.js"
const wa_service = new WhatsappService()


document.addEventListener("DOMContentLoaded", () => {
    const whatsappButton = document.getElementById("whatsapp_button")
    wa_service.redirectToWA(whatsappButton, 0)
})

function toggleElementByClick(element_id, tailwind_class) {
    const element = document.getElementById(element_id)
    element.classList.toggle(tailwind_class)

    const backdrop = document.getElementById(`${element_id}_backdrop`)
    if (backdrop) {
        backdrop.classList.toggle("hidden")
    }
}

window.toggleElementByClick = toggleElementByClick
