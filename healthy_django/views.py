from healthy_django.conf import HEALTH_CHECK
from django.http.response import HttpResponse, JsonResponse
from django.views import View


class HealthCheckView(View):
    def get(self, request):
        results = []
        status_code = 200
        for check in HEALTH_CHECK:
            if check.exclude_main:
                continue
            status = check.health_status()
            results.append(status)
            status_code = max(status["code"], status_code)
        return JsonResponse({"health": results}, status=status_code)


class HealthCheckInduvidualView(View):
    def get(self, request, health):
        status = health.health_status()
        status_code = status["code"]
        return JsonResponse({"health": status}, status=status_code)