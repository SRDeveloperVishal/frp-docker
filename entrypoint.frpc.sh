#!/bin/sh

echo "⚙️  Generating frpc.toml from hosts file..."
python3 /frp/generate_frpc.py

echo "🚀 Starting FRPC..."
exec /frp/frpc -c /frp/config/frpc.toml
