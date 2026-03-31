#!/bin/sh

set -e

# activate the virtual environment
. /app/venv/bin/activate

# ensure migrations are created
python3 manage.py makemigrations

# list migrations
python3 manage.py showmigrations

# perform the migrations
python manage.py migrate --noinput

# list migrations
python3 manage.py showmigrations