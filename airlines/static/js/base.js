document.addEventListener("DOMContentLoaded", () => {

    const openMenu = document.getElementById("btn_open_menu")
    const sideNavbarMenu = document.getElementById("side_navbar_menu")
    const closeMenu = document.getElementById("btn_close_menu")

    openMenu.addEventListener("click", () => {
        sideNavbarMenu.classList.toggle("translate-x-full")
    })

    closeMenu.addEventListener("click", () => {
        sideNavbarMenu.classList.toggle("translate-x-full")
    })

})
