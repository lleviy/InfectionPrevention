
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from django.db import models
from django.core import validators
from django.contrib.auth.models import BaseUserManager

from utils.geolocation import fetch_district, fetch_coordinates


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=10, blank=True)
    email = models.EmailField(
        validators=[validators.validate_email],
        unique=True,
        blank=False
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    birth_date = models.DateField(blank=True, null=True)
    children = models.BooleanField(default=False)
    address = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=50, blank=True)
    okrug = models.CharField(max_length=100, blank=True)
    lat = models.DecimalField(max_digits=15, decimal_places=13, null=True, blank=True)
    lon = models.DecimalField(max_digits=15, decimal_places=13, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    recommendations = models.TextField(max_length=300, blank=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)

    subscribed_to_newsletter = models.BooleanField(default=False)

    NEWSLETTER_CHOICES = [
        ('email', 'Электронная почта'),
        ('phone', 'СМС'),
    ]

    newsletter_choice = models.CharField(
        max_length=8,
        choices=NEWSLETTER_CHOICES,
        default='email',
    )

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list

    telegram_id = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.email

    @property
    def full_name(self):
        if self.user.first_name:
            return self.first_name + self.last_name
        return self.user.email

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)


# @receiver(pre_save, sender=UserProfile)
def user_profile_pre_save(sender, instance, **kwargs):
    if instance.address:
        instance.district, instance.okrug = fetch_district(instance.address)
        instance.lat, instance.lon = fetch_coordinates(instance.address)


pre_save.connect(user_profile_pre_save, sender=UserProfile)
