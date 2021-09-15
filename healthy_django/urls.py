# -*- coding: utf-8 -*-
import healthy_django
from healthy_django.views import HealthCheckView
from django.conf.urls import url
from django.views.generic import TemplateView


app_name = "healthy_django"
urlpatterns = [
    url(r"", HealthCheckView.as_view()),
]
