from __future__ import absolute_import

import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InfectionPrevention.settings')

app = Celery('InfectionPrevention')
app.config_from_object('django.conf:settings')
app.conf.beat_schedule = {
    # Executes every Monday morning at 10:30 a.m.
    'update-recommendations': {
        'task': 'accounts.tasks.update_recommendations',
        'schedule': crontab(hour=10, minute=30, day_of_week=1),
    },
}
app.autodiscover_tasks()
