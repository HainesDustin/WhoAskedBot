#!/bin/bash

# Create virtual environment
python -m venv ./venv --clear

# Install dependencies
./venv/Scripts/pip install -r depends

# Create .env
echo "DISCORD_TOKEN=" > .env