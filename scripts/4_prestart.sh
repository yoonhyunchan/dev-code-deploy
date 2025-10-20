#! /usr/bin/env bash

set -e
set -x

source .venv/bin/activate


# Let the DB start
python app/backend_pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python app/initial_data.py
