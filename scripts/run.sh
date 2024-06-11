#! /usr/bin/env bash

source .env
source venv/bin/activate
cd src
fastapi dev main.py
deactivate
