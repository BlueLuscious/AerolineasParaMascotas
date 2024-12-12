# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# destinatarios = config.email
# asunto = "Prueba"
# cuerpo = "Este es un mensaje de prueba"

# # Configuración del servidor SMTP
# smtp_host = "mail.qualitypost.com.mx"
# smtp_port = 465
# smtp_user = "adcash"
# smtp_pass = "Flo2ER89gDN9"

# # Crear el mensaje
# msg = MIMEMultipart()
# msg['From'] = 'adcash@qualitypost.com.mx'
# msg['To'] = ','.join(destinatarios)  # destinatarios debe ser una lista de correos electrónicos
# msg['Subject'] = asunto

# # Cuerpo del mensaje
# msg.attach(MIMEText(cuerpo, 'html'))

# # Enviar el correo
# try:
#     server = smtplib.SMTP_SSL(smtp_host, smtp_port)
#     server.login(smtp_user, smtp_pass)
#     server.sendmail(msg['From'], destinatarios, msg.as_string())
#     server.quit()
#     print("Correo enviado exitosamente")
# except Exception as e:
#     print(f"Error al enviar el correo: {e}")