import smtplib

# email : notification.raspberrypi001@gmail.com
# email pwd : 3C7cvKfW3gEyc0VoNW28
# app pwd : nmzeslqgencibvhp


import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()

subject = "Email Subject"
body = "This is the body of the text message"
sender = "notification.raspberrypi001@gmail.com"
recipients = ["aabhay@etu.uqac.ca"]
password = "nmzeslqgencibvhp"

send_email(subject, body, sender, recipients, password)