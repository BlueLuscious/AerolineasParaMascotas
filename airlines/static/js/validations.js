export class FormValidations {

    validateFullName(fullNameInput, warning) {
        if (fullNameInput.value == '') {
            warning.innerHTML = 'Nombre completo esta vacío'
            fullNameInput.style.borderBottomColor = 'rgb(180, 20, 60)'
            return false
        } else if (!/^([a-zA-ZáéíóúÁÉÍÓÚüÜñÑ]+\s)*[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ]+$/.test(fullNameInput.value)) {
            warning.innerHTML = 'Nombre completo debe tener solo letras'
            fullNameInput.style.borderBottomColor = 'rgb(180, 20, 60)'
            return false
        } else if (!/^([A-ZÁÉÍÓÚÜÑ][a-záéíóúüñ]+\s)*[A-ZÁÉÍÓÚÜÑ][a-záéíóúüñ]+$/.test(fullNameInput.value)) {
            warning.innerHTML = 'Cada palabra debe comenzar con mayuscula'
            fullNameInput.style.borderBottomColor = 'rgb(180, 20, 60)'
            return false
        }
        fullNameInput.style.borderBottomColor = 'rgb(50, 170, 100)'
        return true
    } // validate lastname function
    
    validateEmail(emailInput, warning) {
        if (emailInput.value == '') {
            warning.innerHTML = 'Email esta vacío'
            emailInput.style.borderBottomColor = 'rgb(180, 20, 60)'
            return false
        } else if (!/^[a-z0-9@.]+$/.test(emailInput.value)) {
            warning.innerHTML = 'Email debe tener letras minusculas y numeros'
            emailInput.style.borderBottomColor = 'rgb(180, 20, 60)'
            return false
        } else if (emailInput) {
            const domains = ['@gmail.com', '@yahoo.com', '@outlook.com']
            let isValid = false

            domains.forEach(function (domain) {
                if (emailInput.value.endsWith(domain)) {
                    isValid = true
                }
            })

            if (!isValid) {
                warning.innerHTML = 'Dominio de email invalido o no aceptado'
                emailInput.style.borderBottomColor = 'rgb(180, 20, 60)'
                return false
            }
        }
        emailInput.style.borderBottomColor = 'rgb(50, 170, 100)'
        return true
    } // validate email function

    validatePhoneNumber(phoneNumberInput, warning) {
        if (phoneNumberInput.value == '') {
            warning.innerHTML = 'Telefono esta vacío'
            phoneNumberInput.style.borderBottomColor = 'rgb(180, 20, 60)'
            return false
        } else if (!/^\d+$/.test(phoneNumberInput.value)) {
            warning.innerHTML = 'Telefeno debe tener solo numeros'
            phoneNumberInput.style.borderBottomColor = 'rgb(180, 20, 60)'
            return false
        } else if (phoneNumberInput.value.length != 10) {
            warning.innerHTML = 'Telefono debe tener 10 digitos'
            phoneNumberInput.style.borderBottomColor = 'rgb(180, 20, 60)'
            return false
        }
        phoneNumberInput.style.borderBottomColor = 'rgb(50, 170, 100)'
        return true
    } // validate phone number function

}