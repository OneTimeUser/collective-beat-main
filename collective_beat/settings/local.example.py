from base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += [
    'django-debug-toolbar'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'local.db',
        'HOST': 'localhost',
        'USER': '',
        'PASSWORD': '',
        'PORT': ''
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your-username@gmail.com'
EMAIL_HOST_PASSWORD = 'your-password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}