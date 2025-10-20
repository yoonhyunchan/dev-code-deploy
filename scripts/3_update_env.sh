#!/bin/bash
REPO_DIR="/opt/dev-code-deploy"

cd $REPO_DIR

source .venv/bin/activate

python app/setting_env.py
