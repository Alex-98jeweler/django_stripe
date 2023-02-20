#!/bin/bash

pip install --upgrade pip
RUN pip install -r requirements.txt
python manage.py flush --no-input
python manage.py migrate

exec "$@"
