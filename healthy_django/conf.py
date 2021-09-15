from healthy_django.healthcheck.django_cache import DjangoCacheHealthCheck
from django.conf import settings
from healthy_django.healthcheck.django_database import DjangoDatabaseHealthCheck

default_configuration = [
    DjangoDatabaseHealthCheck("Database", connection_name="default"),
    DjangoCacheHealthCheck("Cache", connection_name="default"),
]

HEALTH_CHECK = getattr(settings, "HEALTHY_DJANGO", default_configuration)
