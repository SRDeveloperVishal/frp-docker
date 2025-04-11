#!/bin/sh

echo "⚙️  Generating frpc.toml from hosts file..."
python3 /frp/generate_frps.py

echo "🚀 Starting FRPs..."
exec /frp/frps -c /frp/config/frps.toml
