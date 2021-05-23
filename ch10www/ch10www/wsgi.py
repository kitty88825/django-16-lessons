"""
WSGI config for ch10www project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/kitty88825/ch10www'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ch10www.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
