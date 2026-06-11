# flake8: noqa
# pylint: disable=wildcard-import, unused-wildcard-import

import dj_database_url
from decouple import config

from .base import *


DEBUG = False

DATABASES = {
    'default': dj_database_url.parse(
        config('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

ADMINS = ['helrich.bzm@gmail.com']
MANAGERS = ADMINS

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
