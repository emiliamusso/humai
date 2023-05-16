import os
import smtplib
from email.message import EmailMessage

# Usuario y contraseña
user_gmail = os.env('USER_GMAIL')
password_gmail = os.env('PASSWORD_GMAIL')

def send_notifying_mail(mail_user: str = "", mail_password: str = "") -> None:
  msg = EmailMessage()
# Contenido
  msg['From']= mail_user
  msg['To']="emmimusso@gmail.com"
  msg['Subject']= "Probando mandar mails!"
  cuerpo_del_mail = 'Este es un mail enviado con Python en la clase! =D'
  msg.set_content(cuerpo_del_mail)
  
# No se queden en los detalles aquí, pero pueden leer más sobre el protocolo SMTP acá: https://es.wikipedia.org/wiki/Protocolo_para_transferencia_simple_de_correo 
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()

  server.login(mail_user, mail_password)

# enviar
  server.send_message(msg)
  server.quit();


send_notifying_mail(user_gmail, password_gmail)

  if __name__ == "__main__":
      enviar_mail(user_gmail, password_gmail) # modificar segun se llame tu funcion y parametros
