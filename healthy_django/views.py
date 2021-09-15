from django.http.response import HttpResponse, JsonResponse
from django.views import View

from healthy_django.healthcheck.django_database import DjangoDatabaseHealthCheck


class HealthCheckView(View):
    def get(self, request):
        return JsonResponse(DjangoDatabaseHealthCheck("Database", connection_name="default").health_status())
