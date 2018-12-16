"""Módulo de configuração celery."""

import os

import celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')

app = celery.Celery('projeto')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
