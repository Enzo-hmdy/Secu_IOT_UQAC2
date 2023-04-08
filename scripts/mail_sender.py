import smtplib

# email : notification.raspberrypi001@gmail.com
# email pwd : 3C7cvKfW3gEyc0VoNW28
# app pwd : nmzeslqgencibvhp

import smtplib
from email.mime.text import MIMEText

# méthode envoi de mail par défaut
def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()

# méthode envoi de mail avec quelques paramètres déjà remplis
# utilisez celui-ci pour l'envoi de notification
def notify(recipient_mail, detected_label):
    subject = "[Raspberry Pi] Détection d'une attaque"
    sender = "notification.raspberrypi001@gmail.com"
    password = "nmzeslqgencibvhp"
    recipients = [recipient_mail]
    body = "ATTENTION!\nLa machine [Raspberry Pi] a détecté un cyber attaque de type : "+detected_label+"\nVeuillez mettre en place un système de prévention."
    send_email(subject, body, sender, recipients, password)

# test
recipient = "aabhay@etu.uqac.ca"
notify(recipient,"Keylog")