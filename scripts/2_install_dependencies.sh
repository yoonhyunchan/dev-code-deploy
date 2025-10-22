#!/bin/bash
REPO_DIR="/opt/backend"

cd $REPO_DIR

# 1. 가상 환경 생성 및 활성화
/usr/bin/python3.11 -m venv .venv
source .venv/bin/activate

# 2. uv 및 argon2 설치 (설치 스크립트와 동일)
pip install uv 

# 3. 프로젝트 종속성 동기화
uv sync

pip install argon2-cffi dotenv boto3
