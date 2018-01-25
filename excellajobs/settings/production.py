from __future__ import absolute_import, unicode_literals
from .base import *

import os
import dj_database_url

try:
    from .local import *
except ImportError:
    pass

DEBUG = False
SECRET_KEY = os.getenv('SECRET_KEY')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = get_env_setting('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = get_env_setting('SENDGRID_PASSWORD')
EMAIL_PORT = 587 