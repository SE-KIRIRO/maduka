import os
from celery import Celery

# set the default django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myduka.settings')
app = Celery('myduka')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()