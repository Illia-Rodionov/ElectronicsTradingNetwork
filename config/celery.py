import os
from celery import Celery
from celery.schedules import crontab

from config.settings import CELERY_BROKER_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery("config", broker=CELERY_BROKER_URL, include=['core.tasks'])
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add_every_3_hours': {
        'task': "core.tasks.add_or_subtract_random_numbers_from_debt",
        'schedule': crontab(minute=0, hour='*/3'),
        'args': (5, 500)
    },
    'every_day_6.30': {
        'task': "core.tasks.add_or_subtract_random_numbers_from_debt",
        'schedule': crontab(hour=6, minute=30),
        'args': (-10000, -100)
    },
}