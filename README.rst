=====
Boter
=====

Polls is a simple Django app to interact with telegram

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'boter',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^boter/', include('boter.urls')),

3. Run `python manage.py migrate` to create the boter models.