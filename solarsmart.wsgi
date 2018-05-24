import os
import sys

sys.path.append('/var/www/html/oxyelite.com/public_html/solarsmart-')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
