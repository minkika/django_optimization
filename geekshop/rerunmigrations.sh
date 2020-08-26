#!/bin/bash
find authapp/migrations ! -name '__init__.py' -type f -exec rm -f {} +
find basketapp/migrations ! -name '__init__.py' -type f -exec rm -f {} +
find mainapp/migrations ! -name '__init__.py' -type f -exec rm -f {} +
find adminapp/migrations ! -name '__init__.py' -type f -exec rm -f {} +
python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py fill

echo 'http://127.0.0.1:8000/admin/'