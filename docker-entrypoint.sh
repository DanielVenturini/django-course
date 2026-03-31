#!/bin/sh

set -e

# activate the virtual environment
. /app/venv/bin/activate

export PYTHONPATH=/app/venv/lib/python3.12/site-packages/

gunicorn application.wsgi:application \
	-b :8080 \
	--control-socket /app/gunicorn.ctr \
	--access-logfile -