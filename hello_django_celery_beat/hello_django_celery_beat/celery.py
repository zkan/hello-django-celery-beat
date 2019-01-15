import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app = Celery('my_django_celery_beat')
app.conf.broker_url = 'redis://localhost:6379/0'
app.autodiscover_tasks()
