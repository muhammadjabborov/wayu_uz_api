from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'schedule_posts': {
        'task': 'get_instagram_posts',
        'schedule': crontab(day_of_week=1)
    },
}
