#!/bin/bash
set -e # Exit immediately if a command fails

echo "--- Custom Entrypoint Script ---"
echo "Argument received, port=$1"

# Action 1: Collect Static
echo "Running collectstatic..."
python manage.py collectstatic --noinput

# Action 2: Database Migrations
echo "Running makemigrations..."
# Note: Usually done in dev, but running here as requested
python manage.py makemigrations

echo "Running migrate..."
python manage.py migrate

# Action 3: Create Superuser (Idempotent)
echo "Checking for superuser creation..."
# We use || true to prevent the script from crashing if the superuser already exists
if [[ -n "$DJANGO_SUPERUSER_USERNAME" ]] && [[ -n "$DJANGO_SUPERUSER_PASSWORD" ]]; then
    python manage.py createsuperuser --noinput || echo "Superuser already exists or creation skipped."
else
    echo "Skipping superuser creation: Environment variables not set."
fi

# Action 4: Start Server
echo "Starting Gunicorn on port $1..."
exec gunicorn main.wsgi:application --bind 0.0.0.0:$1
