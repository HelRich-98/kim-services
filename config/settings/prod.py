# flake8: noqa
# pylint: disable=wildcard-import, unused-wildcard-import

from .base import *


DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "dbname",
        "USER": "dbuser",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
