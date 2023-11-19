from .common import *
import logging.config

DEBUG = True
SECRET_KEY = 'django-insecure-secret-key'

LOGGING_CONFIG = None
logging.config.fileConfig('logging.conf')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django',
        'HOST': 'database',
        'USER': 'django',
        'PASSWORD': 'django',
        'PORT': '5432'
    }
}
