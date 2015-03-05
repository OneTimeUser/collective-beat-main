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

# the developer's Braintree account for sandbox testing
# set False if production and real credentials below
BRAINTREE_SANDBOX = True
BRAINTREE_MERCHANT_ID = 'bppkdhsntngxw7ns'
BRAINTREE_PUBLIC_KEY = '9wck3d59gg7bnskr'
BRAINTREE_PRIVATE_KEY = '3929b5f7486738bd8581b31d645efddc'