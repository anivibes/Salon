#!/bin/bash

# Make script executable
chmod +x runserver.sh

# Navigate to project directory
cd barbershop

# Check if port is provided as an argument
if [ -z "$1" ]; then
  PORT=8000
else
  PORT=$1
fi

# Run server
echo "Starting server on http://localhost:$PORT"
python manage.py runserver 0.0.0.0:$PORT