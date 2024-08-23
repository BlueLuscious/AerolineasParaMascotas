import { WhatsappService } from "./services/whatsapp_service.js"
const wa_service = new WhatsappService()

document.addEventListener("DOMContentLoaded", () => {

    const openMenu = document.getElementById("btn_open_menu")
    const sideNavbarMenu = document.getElementById("side_navbar_menu")
    const closeMenu = document.getElementById("btn_close_menu")

    toggleNavbarByClick(openMenu, sideNavbarMenu)
    toggleNavbarByClick(closeMenu, sideNavbarMenu)

    
    const whatsappButton = document.getElementById("whatsapp_button")
    wa_service.redirectToWA(whatsappButton, 0)

})

function toggleNavbarByClick(button, navbar) {
    button.addEventListener("click", () => {
        navbar.classList.toggle("translate-x-full")
    })
}
