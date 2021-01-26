#!/bin/sh

#COSTANTS
PROJECT_DIR=$(pwd)

#Installing dependencies
[ -x "$(command -v virtualenv )"] || pip install virtualenv && virtualenv venv



$PROJECT_DIR/venv/bin/pip3 install -r requirements.txt

$PROJECT_DIR/venv/bin/python3 $PROJECT_DIR/web/manage.py makemigrations
$PROJECT_DIR/venv/bin/python3 $PROJECT_DIR/web/manage.py migrate
$PROJECT_DIR/venv/bin/python3 $PROJECT_DIR/web/manage.py runserver 9090

