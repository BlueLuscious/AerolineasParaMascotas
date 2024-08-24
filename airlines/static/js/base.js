import { WhatsappService } from "./services/whatsapp_service.js"
const wa_service = new WhatsappService()

document.addEventListener("DOMContentLoaded", () => {

    const openMenu = document.getElementById("btn_open_menu")
    const sideNavbarMenu = document.getElementById("side_navbar_menu")
    const closeMenu = document.getElementById("btn_close_menu")

    toggleElementByClick(openMenu, sideNavbarMenu, "translate-x-full")
    toggleElementByClick(closeMenu, sideNavbarMenu, "translate-x-full")

    
    const whatsappButton = document.getElementById("whatsapp_button")
    wa_service.redirectToWA(whatsappButton, 0)
    
    
    /* SubMenu Servicios */
    const navItemServices = document.getElementById("nav_item_services")
    const navItemServicesContent = navItemServices.querySelector(".item_content")
    const sub_menu = navItemServices.querySelector(".sub_menu")
    const closeSubMenu = document.getElementById("btn_close_sub_menu")

    toggleElementByClick(navItemServicesContent, sub_menu, "hidden")
    toggleElementByClick(closeSubMenu, sub_menu, "hidden")


})

function toggleElementByClick(button, element, tailwind_class) {
    button.addEventListener("click", () => {
        element.classList.toggle(tailwind_class)
    })
}
