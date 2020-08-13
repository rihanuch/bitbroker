release: python manage.py migrate
web: gunicorn bitbroker.wsgi
worker: python manage.py runbot