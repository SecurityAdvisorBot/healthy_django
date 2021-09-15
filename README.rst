=============================
healthy_django
=============================

.. image:: https://badge.fury.io/py/healthy_django.svg
    :target: https://badge.fury.io/py/healthy_django

.. image:: https://travis-ci.org/vigneshhari/healthy_django.svg?branch=master
    :target: https://travis-ci.org/vigneshhari/healthy_django

.. image:: https://codecov.io/gh/vigneshhari/healthy_django/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/vigneshhari/healthy_django

Simple Re Usable tool for Django Healthchecks

Documentation
-------------

The full documentation is at https://healthy_django.readthedocs.io.

Quickstart
----------

Install healthy_django::

    pip install healthy_django

Add it to your `INSTALLED_APPS`:

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

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
