#! /usr/bin/env bash

python3 manage.py migrate

exec "$@"
