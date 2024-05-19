# juntagrico-badges

[![image](https://github.com/juntagrico/juntagrico-badges/actions/workflows/juntagrico-ci.yml/badge.svg?branch=main&event=push)](https://github.com/juntagrico/juntagrico-badges/actions/workflows/juntagrico-ci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/4e1874454ccc91505707/maintainability)](https://codeclimate.com/github/juntagrico/juntagrico-badges/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/4e1874454ccc91505707/test_coverage)](https://codeclimate.com/github/juntagrico/juntagrico-badges/test_coverage)
[![image](https://img.shields.io/github/last-commit/juntagrico/juntagrico-badges.svg)](https://github.com/juntagrico/juntagrico-badges)
[![image](https://img.shields.io/github/commit-activity/y/juntagrico/juntagrico-badges)](https://github.com/juntagrico/juntagrico-badges)

Add badges to members in juntagrico.

This is an extension for juntagrico. You can find more information about juntagrico here
(https://github.com/juntagrico/juntagrico)

## Features

* Badges can be added in the data administration
* Members have a new menu "Badges" where they can see their assigned badges
* The admin can configure for each badge if members can assign them themselves
* The Admin can see a list of all members having badges which he can filter and send emails to matching members

## Installation


Install juntagrico-badge via `pip`

    $ pip install juntagrico-badges

or add it in your projects `requirements.txt`

In `settings.py` add `'juntagrico_badges',`, **above** `'juntagrico''`.

```python
INSTALLED_APPS = [
    ...
    'juntagrico_badges',
    'juntagrico',
]
```

In your `urls.py` you also need to extend the pattern:

```python
urlpatterns = [
    ...
    path('', include('juntagrico_badges.urls')),
]
```
