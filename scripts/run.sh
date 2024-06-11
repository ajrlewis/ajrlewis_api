#! /usr/bin/env bash

source .env
source venv/bin/activate
cd api
fastapi dev main.py
deactivate
