from django.contrib.auth.forms import UserCreationForm
from accounts.models import User, UserProfile
from django import forms

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'birth_date', 'address', 'children', 'subscribed_to_newsletter',
                  "newsletter_choice", "phone_number"]
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'birth_date': 'Дата рождения', 'address': 'Адрес',
                  'children': 'Наличие детей', 'subscribed_to_newsletter': 'Подписаться на рассылку?',
                  "newsletter_choice": 'Куда производить рассылку', "phone_number": 'Номер телефона'}

