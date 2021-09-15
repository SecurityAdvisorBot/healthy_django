=====
Usage
=====

To use healthy_django in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'healthy_django.apps.HealthyDjangoConfig',
        ...
    )

Add healthy_django's URL patterns:

.. code-block:: python

    from healthy_django import urls as healthy_django_urls


    urlpatterns = [
        ...
        url(r'^', include(healthy_django_urls)),
        ...
    ]
