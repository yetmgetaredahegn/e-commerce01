web: gunicorn storefront.wsgi
release: python manage.py migrate
worker: celery -A storefront worker --loglevel=info
