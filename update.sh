#!/bin/sh

if command -v docker-compose > /dev/null 2>&1; then
    echo "Using docker-compose"
    docker-compose down
    docker-compose up -d --build
elif docker compose version > /dev/null 2>&1; then
    echo "Using docker compose"
    docker compose down
    docker compose up -d --build
else
    echo "Neither docker-compose nor docker compose found!"
    exit 1
fi
