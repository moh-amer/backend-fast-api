#!/bin/bash

# Install dependencies if not already installed
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
    source venv/bin/activate
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# Run the application
echo "Starting the application..."
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000