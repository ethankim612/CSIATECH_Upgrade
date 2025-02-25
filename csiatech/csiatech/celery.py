from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csiatech.settings')

app = Celery('csiatech')

# Update the Celery configuration
app.conf.update(
    broker_url='redis://localhost:6379',
    accept_content=['application/json'],
    result_serializer='json',
    task_serializer='json',
    result_backend='django-db',
    timezone='Asia/Seoul',
    broker_connection_retry_on_startup=True,  # New setting to replace the deprecated one
)

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f"Request: {self.request!r}")