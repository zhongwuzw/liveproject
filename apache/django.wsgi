import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'liveproject.settings'

sys.path.append('E:/liveproject')
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()