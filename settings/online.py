# -*- coding:utf8 - *-

from .import *

DEBUG = False
ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '11',
        'USER': 'robot',
        'PASSWORD': 'robot',
        'HOST': "127.0.0.1",
        'PORT': '3306',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'KEY_PREFIX': "newsshop",
    }
}

