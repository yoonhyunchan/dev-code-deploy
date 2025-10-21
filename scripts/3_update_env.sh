#!/bin/bash
REPO_DIR="/opt/app"

cd $REPO_DIR

source .venv/bin/activate

python app/setting_env.py
