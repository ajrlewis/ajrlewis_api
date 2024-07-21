#!/usr/bin/env bash

rm -rf venv
rm -rf public
rm -rf src/alembic
rm src/alembic.ini
find . -type d -name "__pycache__" -exec rm -rf {} +
