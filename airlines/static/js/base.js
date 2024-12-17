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
    
    /* SubMenu Previo a volar */
    const navItemBeforeFly = document.getElementById("nav_item_before_fly")
    const navItemBeforeFlyContent = navItemBeforeFly.querySelector(".item_content")
    const subMenu = navItemBeforeFly.querySelector(".sub_menu")
    const closeSubMenu = document.getElementById("btn_close_sub_menu")
    
    toggleElementByClick(navItemBeforeFlyContent, subMenu, "hidden")
    toggleElementByClick(closeSubMenu, subMenu, "hidden")
    
    /* SubMenu Previo a volar Mobile */
    const navItemBeforeFlyMobile = document.getElementById("nav_item_before_fly_mobile")
    const navItemBeforeFlyContentMobile = navItemBeforeFlyMobile.querySelector(".item_content")
    const subMenuMobile = navItemBeforeFlyMobile.querySelector(".sub_menu")
    const navItemBeforeFlyContentArrow = navItemBeforeFlyContentMobile.querySelector(".arrow")

    toggleElementByClick(navItemBeforeFlyContentArrow, subMenuMobile, "hidden")
    toggleElementByClick(navItemBeforeFlyContentArrow, navItemBeforeFlyContentArrow, "rotate-180")

})

function toggleElementByClick(button, element, tailwind_class) {
    button.addEventListener("click", () => {
        element.classList.toggle(tailwind_class)
    })
}
