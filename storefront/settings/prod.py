from storefront.settings.dev import SECRET_KEY
from .common import *
import os
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['.onrender.com']

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

REDIS_URL = os.environ['REDIS_URL']
CELERY_BROKER_URL = REDIS_URL


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}