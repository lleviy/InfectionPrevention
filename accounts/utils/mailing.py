from InfectionPrevention.settings import get_secret
from accounts.utils import mainsms


def send_sms(phone, recommendations):
    project = 'firstproject__1'  # Имя проекта
    api_key = get_secret("SMS_API_KEY")  # API-ключ
    sms = mainsms.SMS(project, api_key)  # Создаём объект
    sms.sendSMS(phone, recommendations)