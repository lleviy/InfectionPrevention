from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import UserManager, User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

import jwt

from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


from django.contrib.auth.models import BaseUserManager


# class UserManager(BaseUserManager):
#     """
#     Django требует, чтобы пользовательские `User`
#     определяли свой собственный класс Manager.
#     Унаследовав от BaseUserManager, мы получаем много кода,
#     используемого Django для создания `User`.
#
#     Все, что нам нужно сделать, это переопределить функцию
#     `create_user`, которую мы будем использовать
#     для создания объектов `User`.
#     """
#
#     def create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError(_('email is required'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(('superuser must have is_staff=True.'))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(('superuser must have is_superuser=True.'))
#         return self.create_user(email, password, **extra_fields)
#
#
class User(AbstractUser):
    # username = models.CharField(
    #     ('username'),
    #     max_length=150,
    #     unique=True,
    #     blank=True,
    #     null=True,
    #     help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    #     error_messages={
    #         'unique': ("A user with that username already exists."),
    #     },
    # )
    email = models.EmailField(
        validators = [validators.validate_email],
        unique=True,
        blank=False
        )
    # first_name = models.CharField(max_length=20, blank=True)
    # last_name = models.CharField(max_length=20, blank=True)
    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    # Свойство `USERNAME_FIELD` сообщает нам, какое поле мы будем использовать для входа.
    REQUIRED_FIELDS = ['email',]
    # Сообщает Django, что класс UserManager, определенный выше,
    # должен управлять объектами этого типа.
    # objects = UserManager()
    # def __str__(self):
    #     """
    #     Возвращает строковое представление этого `User`.
    #     Эта строка используется, когда в консоли выводится `User`.
    #     """
    #     return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    birth_date = models.DateField(blank=True, null=True)
    children = models.BooleanField(default=False)
    # к этому полю подключить карты
    location = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    recommendations = models.TextField(max_length=300, blank=True)
    subscribed_to_newsletter = models.BooleanField(default=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

