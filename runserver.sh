#!/bin/bash

# -------------------------------------------------
# Royal Cuts Barber Shop - Local Development Script
# -------------------------------------------------
# This script sets up and runs the Royal Cuts application locally
# It checks for dependencies, sets up the environment, and starts the server

# Text formatting
BOLD="\033[1m"
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
BLUE="\033[0;34m"
RED="\033[0;31m"
NC="\033[0m" # No Color

echo -e "${BOLD}${BLUE}╔═══════════════════════════════════════════╗${NC}"
echo -e "${BOLD}${BLUE}║            ROYAL CUTS BARBER SHOP          ║${NC}"
echo -e "${BOLD}${BLUE}║                Local Setup                 ║${NC}"
echo -e "${BOLD}${BLUE}╚═══════════════════════════════════════════╝${NC}"
echo

# Function to check if Python module is installed
module_installed() {
  python -c "import $1" 2>/dev/null
  return $?
}

# Function to check if a command exists
command_exists() {
  command -v "$1" >/dev/null 2>&1
}

# Check if Python is installed
if ! command_exists python && ! command_exists python3; then
  echo -e "${RED}Error: Python is not installed. Please install Python 3.10 or higher.${NC}"
  exit 1
fi

# Determine Python command (python or python3)
if command_exists python3; then
  PYTHON_CMD=python3
else
  PYTHON_CMD=python
fi

echo -e "${YELLOW}Using Python command: ${PYTHON_CMD}${NC}"

# Check Python version
PY_VERSION=$($PYTHON_CMD -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo -e "${YELLOW}Python version: ${PY_VERSION}${NC}"

# Parse major and minor version
PY_MAJOR=$(echo $PY_VERSION | cut -d'.' -f1)
PY_MINOR=$(echo $PY_VERSION | cut -d'.' -f2)

# Check if Python version is at least 3.10
if [ "$PY_MAJOR" -lt 3 ] || ([ "$PY_MAJOR" -eq 3 ] && [ "$PY_MINOR" -lt 10 ]); then
  echo -e "${RED}Error: Python 3.10 or higher is required. Current version: ${PY_VERSION}${NC}"
  echo -e "${YELLOW}Please upgrade your Python installation.${NC}"
  exit 1
fi

# Activate virtual environment if it exists
if [ -d "venv" ]; then
  echo -e "${GREEN}Activating virtual environment...${NC}"
  source venv/bin/activate
else
  echo -e "${YELLOW}No virtual environment found. You may want to create one:${NC}"
  echo -e "  ${PYTHON_CMD} -m venv venv"
  echo -e "  source venv/bin/activate (Linux/macOS) or venv\\Scripts\\activate (Windows)"
  echo
fi

# Check for dependencies and install if necessary
echo -e "${YELLOW}Checking for required Python packages...${NC}"
declare -a MODULES=("django" "psycopg2" "requests" "dotenv")
for MODULE in "${MODULES[@]}"; do
  # Handle special cases for import names
  IMPORT_NAME=$MODULE
  if [ "$MODULE" = "psycopg2" ]; then
    PACKAGE_NAME="psycopg2-binary"
  elif [ "$MODULE" = "dotenv" ]; then
    IMPORT_NAME="dotenv"
    PACKAGE_NAME="python-dotenv"
  else
    PACKAGE_NAME=$MODULE
  fi

  if ! module_installed $IMPORT_NAME; then
    echo -e "  ${YELLOW}Installing ${PACKAGE_NAME}...${NC}"
    pip install $PACKAGE_NAME
  else
    echo -e "  ${GREEN}✓ ${PACKAGE_NAME} is already installed.${NC}"
  fi
done

# Check if .env file exists
if [ ! -f ".env" ]; then
  echo -e "${YELLOW}No .env file found. Creating a default one...${NC}"
  cat > .env << EOF
# Supabase connection details (required)
SUPABASE_URL=https://phuhhrqzzqdfheuhqofi.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBodWhocnF6enFkZmhldWhxb2ZpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDI3NTAyMjEsImV4cCI6MjA1ODMyNjIyMX0.b4KLx3W1wliVO6fgHMaJIqN6vA9F5BMiUFqdD1tmsHo
SUPABASE_SECRET_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBodWhocnF6enFkZmhldWhxb2ZpIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0Mjc1MDIyMSwiZXhwIjoyMDU4MzI2MjIxfQ.HBoktk6j1cBqXbuT1wOwUDRsCAwMTDKyXC_qxs7n474

# Django settings (optional)
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=django-insecure-q&kzhu^6j5%n#ioc!2nh+9z4!yj-0kbxf+0!0c9_3qt-v3p=j&
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
DJANGO_CSRF_TRUSTED_ORIGINS=https://*.replit.dev,https://*.replit.app,http://localhost:8000,http://127.0.0.1:8000

# Server settings (optional)
PORT=8000
EOF
  echo -e "${GREEN}.env file created successfully.${NC}"
else
  echo -e "${GREEN}✓ .env file already exists.${NC}"
fi

# Check if port is provided as an argument, otherwise use .env or default
if [ -z "$1" ]; then
  PORT=$(grep -E "^PORT=" .env 2>/dev/null | cut -d'=' -f2 || echo "8000")
else
  PORT=$1
fi

# Make the script executable for future runs
chmod +x runserver.sh

echo
echo -e "${BOLD}${GREEN}Setup complete!${NC}"
echo -e "${BOLD}${BLUE}Starting the Royal Cuts Barber Shop server...${NC}"
echo

# Start Django server
cd barbershop
echo -e "${GREEN}Server is running at: ${BOLD}http://localhost:${PORT}${NC}"
echo -e "${YELLOW}Press Ctrl+C to stop the server${NC}"
echo
$PYTHON_CMD manage.py runserver 0.0.0.0:${PORT}

# This part will only execute if the server stops
echo
echo -e "${YELLOW}Server has stopped. Thank you for using Royal Cuts!${NC}"