# -*- coding: utf-8 -*-
import healthy_django
from healthy_django.views import HealthCheckView, HealthCheckInduvidualView
from django.urls import path
from django.views.generic import TemplateView
from healthy_django.conf import HEALTH_CHECK


app_name = "healthy_django"
urlpatterns = [
    path("", HealthCheckView.as_view()),
]

for check in HEALTH_CHECK:
    urlpatterns.append(
        path("{0}".format(check.slug), HealthCheckInduvidualView.as_view(), {"health": check}),
    )
