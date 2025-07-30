from storefront.settings.dev import SECRET_KEY
from decouple import config
from .common import *
import os
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['e-commerce01-jzwl.onrender.com']

DATABASES = {
    'default': dj_database_url.parse(config('DATABASE_URL'))
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


# Use getenv for values that can have defaults
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp-relay.brevo.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'

# Use environ for secrets that must exist in production otherwise it crashes
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']        # Required (Brevo login)
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']  # Required (Brevo password)

# Default sender email (fallback provided)
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'yetmgeta.tech@gmail.com')
