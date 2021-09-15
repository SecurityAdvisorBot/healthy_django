from healthy_django.conf import HEALTH_CHECK
from django.http.response import HttpResponse, JsonResponse
from django.views import View


class HealthCheckView(View):
    def get(self, request):
        results = []
        for check in HEALTH_CHECK:
            results.append(check.health_status())
        return JsonResponse({"health": results})
