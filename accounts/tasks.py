from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import UserProfile
from .utils.form_personal_recommendations import form_personal_recommendations
from .utils.mailing import send_mail, send_sms


@shared_task
def update_recommendations(self):
    profiles = UserProfile.objects.all()
    for profile in profiles:
        recommendations = form_personal_recommendations(profile)
        if recommendations != profile.recommendations:
            profile.recommendations = recommendations
            profile.save()
            if profile.subscribed_to_newsletter:
                if profile.newsletter_choice == 'email':
                    send_mail(profile.user.email, 'Новые персональные рекомендации', recommendations)
                elif profile.newsletter_choice == 'phone':
                    send_sms(profile.phone_number, recommendations)
                else:
                    pass

