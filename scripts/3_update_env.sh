#!/bin/bash
REPO_DIR="/opt/backend"

cd $REPO_DIR

source .venv/bin/activate

python app/setting_env.py
