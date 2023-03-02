#!/bin/sh

# Apply database migrations
sudo echo "Apply database migrations"
python manage.py migrate

exec "$@"