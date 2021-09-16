from healthy_django.healthcheck.django_cache import DjangoCacheHealthCheck
from django.conf import settings
from healthy_django.healthcheck.django_database import DjangoDatabaseHealthCheck
from healthy_django.healthcheck.celery_queue_length import DjangoCeleryQueueLengthHealthCheck
from healthy_django.healthcheck.sqs_length import AWSSQSQueueHealthCheck

default_configuration = [
    # DjangoDatabaseHealthCheck("Database", slug="main_database", connection_name="default"),
    # DjangoCacheHealthCheck("Cache", slug="main_cache", exclude_main=True, connection_name="default"),
    # DjangoCeleryQueueLengthHealthCheck(
    #     "Celery Queue Length",
    #     slug="celery_queue",
    #     broker="redis://" + "0.0.0.0" + ":6379",
    #     queue_name="celery",
    #     info_length=10,
    #     warning_length=20,
    #     alert_length=30,
    # ),
    # AWSSQSQueueHealthCheck(
    #     "AWS SQS Queue Length",
    #     slug="aws_sqs_length",
    #     queue_url="",
    #     info_length=10,
    #     warning_length=20,
    #     alert_length=30,
    # ),
]

HEALTH_CHECK = getattr(settings, "HEALTHY_DJANGO", default_configuration)
HEALTHY_DJANGO_AWS_REGION = getattr(settings, "HEALTHY_DJANGO_AWS_REGION", None)
HEALTHY_DJANGO_AWS_ACCESS_KEY = getattr(settings, "HEALTHY_DJANGO_AWS_ACCESS_KEY", None)
HEALTHY_DJANGO_AWS_SECRET = getattr(settings, "HEALTHY_DJANGO_AWS_SECRET", None)
