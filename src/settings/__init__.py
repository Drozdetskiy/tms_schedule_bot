# Application Library
from settings.base import *  # noqa
from settings.celery import app as celery_app

__all__ = ["celery_app"]
