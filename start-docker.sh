#!/bin/bash

if [ -f .env ]; then
    source .env
else
    echo "Error: .env file not found"
    exit 1
fi

ARCH=$(uname -m)
if [[ "$ARCH" == "arm64" ]] || [[ "$ARCH" == "aarch64" ]]; then
    echo "Detected ARM64 architecture"
    export DOCKERFILE=Dockerfile.arm64
else
    echo "Using default Dockerfile"
    export DOCKERFILE=Dockerfile
fi

PROFILES=""

[ "$ENABLE_DB" = "1" ] && PROFILES="$PROFILES --profile db"
[ "$ENABLE_CHATBOT" = "1" ] && PROFILES="$PROFILES --profile chatbot"
[ "$ENABLE_OLLAMA" = "1" ] && PROFILES="$PROFILES --profile ollama"
[ "$ENABLE_BROWSER_UI" = "1" ] && PROFILES="$PROFILES --profile browser-use-webui"

if [ -n "$PROFILES" ]; then
    echo "Starting services with profiles:$PROFILES"
    docker-compose $PROFILES up -d
else
    echo "No services enabled in .env"
    exit 1
fi