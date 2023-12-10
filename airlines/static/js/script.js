import { FormValidations } from "./validations.js"
const validator = new FormValidations

document.addEventListener('DOMContentLoaded', function() {

    const inputs = Array.from(document.getElementsByClassName('form-control'))
    const sendForm = document.getElementById('send_contact_form')
    const warnings = Array.from(document.getElementsByClassName('warning'))
    
    inputs.forEach(function(input, index) {
        input.addEventListener('click', function() {
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
        const body = `Nombre completo: ${fullName}
        Correo Electronico: ${email}
        Telefono: ${phone}`
    
        win=window.open(`mailto:santamarialucio01@gmail.com?subject=Datos de contacto&body=${encodeURIComponent(body)}`,'emailWin')
    }
    /* open emailWin */

})