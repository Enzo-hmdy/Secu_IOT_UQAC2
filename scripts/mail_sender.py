import smtplib

# email : secuiotuqac@gmail.com
# mail pwd : Z4G8zng5atNQL2BPhMCs
# app pwd : qimgsrtsagcixeck

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
    subject = "Détection du Raspberry Pi"
    sender = "secuiotuqac@gmail.com"
    password = "qimgsrtsagcixeck"
    recipients = [recipient_mail]
    body = "\nNous avons détecté une attaque type : "+detected_label+"\n"
    send_email(subject, body, sender, recipients, password)
    print("Mail sent")

# test
recipient = "aabhay@etu.uqac.ca"
notify(recipient,"Test")