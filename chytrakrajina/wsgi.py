"""
WSGI config for chytrakrajina project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from decouple import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chytrakrajina.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", config("DJANGO_CONFIGURATION", default="Dev"))

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()