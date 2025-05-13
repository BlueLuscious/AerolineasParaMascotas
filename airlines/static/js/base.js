import { WhatsappService } from "./services/whatsapp_service.js"
const wa_service = new WhatsappService()

window.redirectToWA = wa_service.redirectToWA.bind(wa_service)
window.toggleElementByClick = toggleElementByClick


document.addEventListener("DOMContentLoaded", () => {
    // Nav-Link Styles & Interactivity
    const sections = document.querySelectorAll("section")
    const navLinks = document.querySelectorAll(".nav_link")
    let current_link = ""

    activeNavLink(navLinks, current_link)
  
    window.addEventListener("scroll", () => {
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100
            if (pageYOffset >= sectionTop) {
                current_link = section.getAttribute("id")
            }
        })
        activeNavLink(navLinks, current_link)
    })
})

/**
 * Beautify nav-links by section.
 * @param {NodeListOf<Element>} nav_links - All Nav-Links
 * @param {string} current_link - Current Nav-Link
 * @returns {void}
 */
function activeNavLink(nav_links, current_link) {
    nav_links.forEach(link => {
        const linkHref = link.getAttribute("href")
        const linkPathname = link.getAttribute("data-pathname")

        link.classList.remove("bg-primary-blue_light", "hover:bg-primary-blue_light", "hover:animate-mini_bounce_fast")
        if (linkHref === `#${current_link}` && window.location.pathname === "/") {
            link.classList.add("bg-primary-blue_light")
        } else if (linkPathname != "/" && linkPathname == window.location.pathname) {
            link.classList.add("bg-primary-blue_light")
        } else {
            link.classList.add("hover:bg-primary-blue_light", "hover:animate-mini_bounce_fast")
        }
    })
}

// Toggle sidemenu
function toggleElementByClick(element_id, tailwind_class) {
    const element = document.getElementById(element_id);
    element.classList.toggle(tailwind_class);

    const backdrop = document.getElementById(`${element_id}_backdrop`)
    if (backdrop) {
        backdrop.classList.toggle(`-${tailwind_class}`);
    }
}
