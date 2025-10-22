#!/bin/bash
REPO_DIR="/opt/backend"

cd $REPO_DIR



# systemd 서비스 파일 생성
# Note: 원본 스크립트에서 파일 생성은 root 권한이 필요합니다.
cat > /etc/systemd/system/myapp.service <<EOF
[Unit]
Description=My Uvicorn App Service
After=network.target

[Service]
User=root
Group=root

# ExecStart 전에 환경 변수 설정
EnvironmentFile=$REPO_DIR/.env

WorkingDirectory=$REPO_DIR
ExecStart=$REPO_DIR/.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# 3. systemd 설정 다시 로드, 서비스 활성화 및 시작
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
