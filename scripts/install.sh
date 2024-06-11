#!/usr/bin/env bash

PYTHON_VERSION=3.9
if [ -d venv ]; then rm -Rf venv; fi
python${PYTHON_VERSION} -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate