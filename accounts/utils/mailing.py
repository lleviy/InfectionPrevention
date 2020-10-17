from django.conf import settings

from InfectionPrevention.settings import get_secret
from accounts.utils import mainsms
import smtplib  # pip install secure-smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_sms(phone, message):
    project = 'firstproject__1'  # Имя проекта
    api_key = get_secret("SMS_API_KEY")  # API-ключ
    sms = mainsms.SMS(project, api_key)  # Создаём объект
    sms.sendSMS(phone, message)


def send_mail(mail, subject, message):
    import smtplib  # pip install secure-smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    msg = MIMEMultipart()
    from_email = settings['EMAIL_USER_HOST']
    password = settings['EMAIL_USER_PASSWORD']

    msg['Subject'] = subject  # Заголовок

    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(from_email, password)
    for mail in open('emails'):
        to_email = mail
        server.sendmail(from_email, to_email, msg.as_string())
    server.quit()