import { FormValidations } from "./validations.js"
const validator = new FormValidations

document.addEventListener('DOMContentLoaded', function() {
    const inputs = Array.from(document.getElementsByClassName('form-control'))
    const sendForm = document.getElementById('send_contact_form')
    const warnings = Array.from(document.getElementsByClassName('warning'))

    const choices = Array.from(document.getElementsByClassName('choices_contact_bar'))
    const emailChoice = document.getElementById('email_choice')
    const whatsappChoice = document.getElementById('whatsapp_choice')
    const choicesDivs = [emailChoice, whatsappChoice]
    
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

    let email_is_active = true
    let whatsapp_is_active = false

    choices.forEach(function(choice, index) {
        choice.addEventListener('click', function() {
            if (index == 0) {
                changeModeActive(choicesDivs[1], choicesDivs[0])
                email_is_active = true
                whatsapp_is_active = false
            }
            if (index == 1) {
                changeModeActive(choicesDivs[0], choicesDivs[1])
                email_is_active = false
                whatsapp_is_active = true
            }
        })
    })

    /* validate form */
    sendForm.addEventListener('click', function(event) {
        const validatedName = validator.validateFullName(inputs[0], warnings[0])
        const validatedEmail = validator.validateEmail(inputs[1], warnings[1])
        const validatedPhone = validator.validatePhoneNumber(inputs[2], warnings[2])

        if (validatedName && validatedEmail && validatedPhone) {
            if (email_is_active){
                openEmail(inputs[0].value, inputs[1].value, inputs[2].value)
            }
            if (whatsapp_is_active) {
                openWhatsApp(inputs[0].value, inputs[1].value, inputs[2].value)
            }
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
        const body = `Nombre completo: ${fullName}.
        Correo Electronico: ${email}.
        Teléfono: ${phone}.`
    
        win=window.open(`mailto:santamarialucio01@gmail.com?subject=Datos de contacto&body=${encodeURIComponent(body)}`,'emailWin')
    }
    /* open emailWin */

    /* open whatsapp */
    function openWhatsApp(fullName, email, phone) {
        const danielPhoneNumber = 5491150599636
        const messageWA = `Datos de contacto:
        Nombre completo: ${fullName}.
        Correo Electronico: ${email}.
        Teléfono: ${phone}.`

        window.open(`https://wa.me/${danielPhoneNumber}/?text=${encodeURIComponent(messageWA)}`)
    }
    /* open whatsapp */

    /* change clases to fake an active mode */
    function changeModeActive(choiceDiv_0, choiceDiv_1) {
        choiceDiv_0.removeAttribute('class')
        choiceDiv_0.className = 'choice_contact_bar'
        choiceDiv_1.removeAttribute('class')
        choiceDiv_1.className = 'choice_contact_bar_alt'
    }
    /* change clases to fake an active mode */

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
        if (window.scrollY > 120) {
            navbar.style.position = 'fixed'
            mainBanner.style.marginTop = '100px'
        }

        if (window.scrollY <= 0) {
            navbar.style.position = 'relative'
            mainBanner.style.marginTop = '0'
        }
    })

    const scrollToTopBtn = document.getElementById('scrollToTop')

    window.addEventListener('scroll', () => {
        const shouldShowButton = window.scrollY > 650
        scrollToTopBtn.disabled = !shouldShowButton
        scrollToTopBtn.style.display = shouldShowButton ? 'block' : false
        scrollToTopBtn.classList.toggle('active', shouldShowButton)
    })

    scrollToTopBtn.addEventListener('click', () => {
        document.body.scrollTop = 0
        document.documentElement.scrollTop = 0
    })
    /* scroll events */

})