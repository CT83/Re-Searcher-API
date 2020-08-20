#!/bin/sh
flask db upgrade
/usr/local/bin/gunicorn --bind 0.0.0.0:8000 wsgi