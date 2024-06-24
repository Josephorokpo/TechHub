#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r alx_ws_project/requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate