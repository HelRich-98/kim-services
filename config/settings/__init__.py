# flake8: noqa
# pylint: disable=wildcard-import, unused-wildcard-import

import os

env = os.getenv("DJANGO_ENV", "dev")

if env == "prod":
    from .prod import *
else:
    from .dev import *
