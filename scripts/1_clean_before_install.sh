#!/bin/bash
# CodeDeploy가 파일을 복사하기 전에 이전 환경을 정리합니다.
REPO_DIR="/opt/backend"

cd $REPO_DIR

# 1. 기존 서비스 중지 (서비스가 이미 존재할 경우)
if sudo systemctl is-active myapp >/dev/null 2>&1; then
    sudo systemctl stop myapp
fi

# 2. 기존 가상 환경 및 .env 파일 정리 (이전 버전의 파일이 남지 않도록)
rm -rf .venv
cp .env.example .env
