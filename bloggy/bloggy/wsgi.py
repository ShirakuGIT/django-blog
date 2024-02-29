"""
WSGI config for bloggy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# bloggy/wsgi.py

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bloggy.settings')

application = get_wsgi_application()

# Automatically create superuser
call_command('create_superuser')
