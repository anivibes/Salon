#!/bin/bash

# Make script executable
chmod +x runserver.sh

# Navigate to project directory
cd barbershop

# Run server
echo "Starting server on http://localhost:8000"
python manage.py runserver 0.0.0.0:8000