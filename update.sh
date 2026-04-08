#!/bin/bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "[mothership] Pulling latest changes..."
git -C "$DIR" pull

echo "[mothership] Stopping old container..."
sudo docker-compose -f "$DIR/docker-compose.yml" down

echo "[mothership] Rebuilding and starting container..."
sudo docker-compose -f "$DIR/docker-compose.yml" up -d --build

echo "[mothership] Done. Container status:"
sudo docker-compose -f "$DIR/docker-compose.yml" ps
