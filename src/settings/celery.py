# Standard Library
import os
from typing import (
    Any,
    Dict,
)

# Third Party Library
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

app = Celery(settings.PROJECT)

SCHEDULE: Dict[str, Any] = {}

app.conf.beat_schedule = SCHEDULE

TASK_ROUTES: Dict[str, Any] = {}

app.config_from_object("django.conf:settings")
app.conf.beat_scheduler = "django_celery_beat.schedulers:DatabaseScheduler"

app.conf.task_default_queue = "default"
app.conf.task_routes = TASK_ROUTES

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
