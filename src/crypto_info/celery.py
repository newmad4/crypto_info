import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crypto_info.settings")
app = Celery("crypto_info")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule["periodic_refresh_exchange_rate"] = {
    "task": "get_newest_exchange_rates",
    "schedule": crontab(minute="0")  # every hour
    # "schedule": crontab(minute="*")  # every minute
}
