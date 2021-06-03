from django.conf import settings
settings.configure()
import smtplib
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from django.contrib.auth.models import User
from django.template.loader import render_to_string
from backoffice.templates import *
#from backoffice.views import MailView




# Create your tests here.



def send_mail():
    try:
        # Connecting
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login("teamsmartalentos@gmail.com", "(sanricardo606%)")
        print('conected....')

# Building message
        mensaje = MIMEText("Este es el mensaje de las narices")
        mensaje['From'] = "teamsmartalentos@gmail.com"
        mensaje['To'] = "frankgalandev@gmail.com"
        mensaje['Subject'] = "Tienes un correo"

    # Envio del mensaje
        mailServer.sendmail("teamsmartalentos@gmail.com", "frankgalandev@gmail.com",
                        mensaje.as_string())

        print('right sent')
    except Exception as e:
        print(e)

#send_mail()


def send_complex_mail():
    try:
# Construimos un mensaje Multipart, con un texto y una imagen adjunta
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login("teamsmartalentos@gmail.com", "(sanricardo606%)")
        print('conected....')

        mensaje = MIMEMultipart()
        mensaje['From']="teamsmartalentos@gmail.com"
        mensaje['To']="frankgalandev@gmail.com"
        mensaje['Subject']="Complex messages for you"
        
        #render_to_string('email_prototype.html')

# Adding text
        mensaje.attach(MIMEText(" This is the fucking  complex message"))

# Adding image
        file = open("backoffice/media/bagmedia.jpg", "rb")
        contenido = MIMEImage(file.read())
        contenido.add_header('Content-Disposition', 'attachment; filename = "bagmedia.jpg"')
        mensaje.attach(contenido)

        # Enviamos el correo, con los campos from y to.
        mailServer.sendmail("teamsmartalentos@gmail.com",
                        "frankgalandev@gmail.com",
                        mensaje.as_string())


        # Cierre de la conexion
        mailServer.close()

        print('right sent')

    except Exception as e:
        print(e)

send_complex_mail()
