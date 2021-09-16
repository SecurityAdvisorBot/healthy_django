from healthy_django.healthcheck.django_cache import DjangoCacheHealthCheck
from django.conf import settings
from healthy_django.healthcheck.django_database import DjangoDatabaseHealthCheck
from healthy_django.healthcheck.celery_queue_length import DjangoCeleryQueueLengthHealthCheck
from healthy_django.healthcheck.sqs_length import AWSSQSQueueHealthCheck

default_configuration = [
    DjangoDatabaseHealthCheck("Database", connection_name="default"),
    DjangoCacheHealthCheck("Cache", connection_name="default"),
    DjangoCeleryQueueLengthHealthCheck(
        "Celery Queue Length",
        broker="redis://" + "0.0.0.0" + ":6379",
        queue_name="celery",
        info_length=10,
        warning_length=20,
        alert_length=30,
    ),
    AWSSQSQueueHealthCheck(
        "AWS SQS Queue Length",
        queue_url="https://sqs.us-west-2.amazonaws.com/632289439953/sa-analytics-dev-enriched",
        info_length=10,
        warning_length=20,
        alert_length=30,
    ),
]

HEALTH_CHECK = getattr(settings, "HEALTHY_DJANGO", default_configuration)
HEALTHY_DJANGO_AWS_REGION = getattr(settings, "HEALTHY_DJANGO_AWS_REGION")
HEALTHY_DJANGO_AWS_ACCESS_KEY = getattr(settings, "HEALTHY_DJANGO_AWS_ACCESS_KEY")
HEALTHY_DJANGO_AWS_SECRET = getattr(settings, "HEALTHY_DJANGO_AWS_SECRET")
