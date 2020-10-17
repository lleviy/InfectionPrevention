from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from .models import UserProfile
from .utils.form_personal_recommendations import form_personal_recommendations


@shared_task
def update_recommendations(self):
    print("update_recommendations")
    profiles = UserProfile.objects.all()
    for profile in profiles:
        recommendations = form_personal_recommendations(profile)
        if recommendations != profile.recommendations:
            profile.recommendations = recommendations
            profile.save()
            # send_mail

