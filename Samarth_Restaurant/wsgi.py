"""
WSGI config for Samarth_Restaurant project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# code changes start here
settings_module = 'Samarth_Restaurant.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'Samarth_Restaurant.settings'



os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', Samarth_Restaurant.settings)

application = get_wsgi_application()
