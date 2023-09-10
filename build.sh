#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install
python gunicorn --chdir ./todo_app.wsgi:application
python manage.py collectstatic --no-input
python manage.py migrate