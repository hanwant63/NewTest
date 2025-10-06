#!/bin/bash

echo "=========================================="
echo "Telegram Bot VPS Deployment Script"
echo "=========================================="
echo ""

# Update system
echo "Step 1: Updating system..."
apt update && apt upgrade -y

# Install Python and dependencies
echo "Step 2: Installing Python..."
apt install python3 python3-pip python3-venv git -y

# Create virtual environment
echo "Step 3: Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment and install packages
echo "Step 4: Installing Python packages..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f .env ]; then
    echo ""
    echo "=========================================="
    echo "⚠️  IMPORTANT: Create .env file"
    echo "=========================================="
    echo "Run this command:"
    echo "nano .env"
    echo ""
    echo "Then add your credentials:"
    echo "API_ID=your_api_id"
    echo "API_HASH=your_api_hash"
    echo "BOT_TOKEN=your_bot_token"
    echo "OWNER_ID=your_telegram_user_id"
    echo ""
    echo "Press Ctrl+X, then Y, then Enter to save"
    echo "=========================================="
else
    echo "✓ .env file found"
fi

# Create systemd service
echo "Step 5: Setting up systemd service..."
CURRENT_DIR=$(pwd)
SERVICE_FILE="/etc/systemd/system/telegram-bot.service"

cat > $SERVICE_FILE <<EOF
[Unit]
Description=Telegram Restricted Content Downloader Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=$CURRENT_DIR
EnvironmentFile=$CURRENT_DIR/.env
ExecStart=$CURRENT_DIR/venv/bin/python $CURRENT_DIR/server.py
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd and enable service
echo "Step 6: Enabling bot service..."
systemctl daemon-reload
systemctl enable telegram-bot.service

echo ""
echo "=========================================="
echo "✅ Deployment Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Make sure .env file is created with your credentials"
echo "2. Start the bot: systemctl start telegram-bot.service"
echo "3. Check status: systemctl status telegram-bot.service"
echo "4. View logs: journalctl -u telegram-bot.service -f"
echo ""
echo "Useful commands:"
echo "  Start:   systemctl start telegram-bot.service"
echo "  Stop:    systemctl stop telegram-bot.service"
echo "  Restart: systemctl restart telegram-bot.service"
echo "  Status:  systemctl status telegram-bot.service"
echo "  Logs:    journalctl -u telegram-bot.service -f"
echo "=========================================="
