Installation
============

Basic Installation
------------------
Install juntagrico-badges with :command:`pip`::

    $ pip install git+https://github.com/juntagrico/juntagrico-badges.git

Django Settings
---------------
You have to add the app to your installed apps in your Django settings

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'juntagrico',
        'juntagrico_badges',
    ]
    
URL Pattern
-----------
You also have to add the following url pattern:

.. code-block:: python

    urlpatterns = [
        ...
        re_path(r'^', include('juntagrico_badges.urls')),
    ]
