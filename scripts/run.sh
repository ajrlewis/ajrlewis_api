#! /usr/bin/env bash

source .env
source venv/bin/activate
# cd api
fastapi dev api/main.py
deactivate
