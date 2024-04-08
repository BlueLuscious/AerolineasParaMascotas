import { FormValidations } from "./validations.js"
const validator = new FormValidations

document.addEventListener('DOMContentLoaded', function() {
    const inputs = Array.from(document.getElementsByClassName('form-control'))
    const sendForm = document.getElementById('send_contact_form')
    const sendWA = document.getElementById('whatsappButton')
    const warnings = Array.from(document.getElementsByClassName('warning'))

    inputs.forEach(function(input, index) {
        input.addEventListener('keydown', function() {
            if (index >= 0) {
                warnings[index].style.display = 'none'
            }
        })
    })

    warnings.forEach(function(warning) {
        warning.style.display = 'none'
    })

    /* validate form */
    sendForm.addEventListener('click', function(event) {
        const validatedName = validator.validateFullName(inputs[0], warnings[0])
        const validatedEmail = validator.validateEmail(inputs[1], warnings[1])
        const validatedPhone = validator.validatePhoneNumber(inputs[2], warnings[2])

        if (validatedName && validatedEmail && validatedPhone) {
            openEmail(inputs[0].value, inputs[1].value, inputs[2].value)
            sendForm.submit()
        } else {
            showWarning(validatedName, warnings[0])
            showWarning(validatedEmail, warnings[1])
            showWarning(validatedPhone, warnings[2])
            event.preventDefault()
        }
    })
    /* validate form */

    /* show warning function */
    function showWarning(value, warning) {
        if (!value) {
            warning.style.display = 'block'
        }
    }
    /* show warning function */

    /* open emailWin */
    function openEmail(fullName, email, phone) {
        // const danielEmail = "servicios@aerolineasparamascotas.com.ar"
        const danielEmail = "contacto@aerolineasparamascotas.com.ar"
        const body = `Nombre completo: ${fullName}.
        Correo Electronico: ${email}.
        Teléfono: ${phone}.`
    
        win=window.open(`mailto:${danielEmail}?subject=Datos de contacto&body=${encodeURIComponent(body)}`,'emailWin')
    }
    /* open emailWin */

    /* open whatsapp */
    sendWA.addEventListener('click', () => {
        openWhatsApp()
    })

    function openWhatsApp() {
        const phoneNumbers = [5491150599636, 5491127142401, 34663418545]
        const messageWA = `Hola, completa con tus datos. Te atenderemos a la brevedad.

Nombre completo:
Correo Electronico:
Teléfono:`

        const seconds = new Date().getSeconds()
        if (seconds >= 0 && seconds <= 9 || seconds >= 30 && seconds <= 39) {
            const currentPhoneNumber = phoneNumbers[0]
            window.location.href = `https://wa.me/${currentPhoneNumber}/?text=${encodeURIComponent(messageWA)}`
        } else if (seconds >= 10 && seconds <= 19 || seconds >= 40 && seconds <= 49) {
            const currentPhoneNumber = phoneNumbers[1]
            window.location.href = `https://wa.me/${currentPhoneNumber}/?text=${encodeURIComponent(messageWA)}`
        } else if (seconds >= 20 && seconds <= 29 || seconds >= 50 && seconds <= 59) {
            const currentPhoneNumber = phoneNumbers[2]
            window.location.href = `https://wa.me/${currentPhoneNumber}/?text=${encodeURIComponent(messageWA)}`
        }
    }
    /* open whatsapp */

    /* reels */
    const reels = Array.from(document.getElementsByClassName('reel'))

    reels.forEach((reel, index) => {
        reel.volume = 0.5

        reel.addEventListener('mouseover', () => {
            if (index >= 0) {
                reel.play()
                reel.muted = false
            }
        })

        reel.addEventListener('mouseout', () => {
            if (index >= 0) {
                reel.currentTime = 0
                reel.pause()
            }
        })
    })
    /*  reel */

    /* scroll events */
    const navbar = document.getElementById('tm-top-bar')
    const mainBanner = document.getElementById('tm-section-1')

    window.addEventListener('scroll', () => {
        if (window.scrollY > 1) {
            navbar.style.position = 'fixed'
            mainBanner.style.marginTop = '100px'

            if (window.innerWidth <= 1200) {
                mainBanner.style.marginTop = '70px'
            }

            if (window.innerWidth <= 991) {
                mainBanner.style.marginTop = '50px'
            }
        }

        if (window.scrollY <= 0) {
            navbar.style.position = 'relative'
            mainBanner.style.marginTop = '0'
        }
    })
    /* scroll events */

})