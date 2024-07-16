#!/bin/bash
set -a

echo "Checking if the .meteorc file exists..."
if [ ! -f ./.meteorc ]; then
    echo "The .meteorc file does not exist. Please create it before running this script."
    exit 1
fi

echo "Sourcing the .meteorc file..."

source ./.meteorc

USER=$(whoami)
GROUP=$(whoami)
USER_ID=$(id -u)
GROUP_ID=$(id -g)

if [ -z "$USER" ]; then
  USER=meteouser
fi

if [ -z "$GROUP" ]; then
  GROUP=meteogroup
fi

if [ -z "$USER_ID" ]; then
  USER_ID=1000
fi

if [ -z "$GROUP_ID" ]; then
  GROUP_ID=1000
fi

export USER GROUP USER_ID GROUP_ID

DEBUG=0
FORCE_RECREATE=""
BUILD=0
MAKEMIGRATIONS=0
MIGRATE=0
CREATESUPERUSER=0
RUNSERVER=0
SHOWHELP=0
NO_FLAGS=1

while [[ $# -gt 0 ]]; do
    case "$1" in
        -d|--debug)
            DEBUG=1
            ;;
        -f|--force)
            FORCE_RECREATE="--force-recreate"
            ;;
        -b|--build)
            BUILD=1
            NO_FLAGS=0
            ;;
        --makemigrations)
            MAKEMIGRATIONS=1
            NO_FLAGS=0
            ;;
        --migrate)
            MIGRATE=1
            NO_FLAGS=0
            ;;
        --createsuperuser)
            CREATESUPERUSER=1
            NO_FLAGS=0
            ;;
        -r|--runserver)
            RUNSERVER=1
            NO_FLAGS=0
          ;;
        -h|--help)
            SHOWHELP=1
            ;;
        *)
            echo "Unknown option: $1, use --help to see the available options."
            exit 1
            ;;
    esac
    shift
done

if [ $SHOWHELP -eq 1 ] || [ $NO_FLAGS -eq 1 ]; then
    echo "Usage: ./start.sh [OPTIONS]"
    echo "Options:"
    echo "  -d, --debug         Run the server in debug mode."
    echo "  -f, --force         Force recreate the containers."
    echo "  -b, --build         Build the containers."
    echo "  --makemigrations    Create the database migrations."
    echo "  --migrate           Run the database migrations."
    echo "  --createsuperuser   Create the superuser."
    echo "  -r, --runserver     Run the backend server."
    echo "  -h, --help          Show this help message."
    exit 0
fi

if [ ! -d "$HOME/meteo-database" ]; then
    echo "Creating the $HOME/meteo-database directory..."
    mkdir -p $HOME/meteo-database
fi

if [ ! -d "./static/admin" ]; then
    echo "Creating the ./static/* directories..."
    mkdir -p ./static/admin
    mkdir -p ./static/rest_framework
fi

if [ $DEBUG -eq 1 ]; then
    export BACKEND_RUN_SRVR_COMMAND="python manage.py runserver 0.0.0.0:8000"
fi

  # Production settings if DEBUG is not set


if [ $BUILD -eq 1 ]; then
    echo "Building the containers..."
    docker compose -f docker-compose.yml -p meteo build
fi

if [ $MAKEMIGRATIONS -eq 1 ]; then
    echo "Creating the database migrations..."
    docker compose -f docker-compose.yml -p meteo run --rm backend python manage.py makemigrations
fi

if [ $MIGRATE -eq 1 ]; then
    echo "Running the database migrations..."
    docker compose -f docker-compose.yml -p meteo run --rm backend python manage.py migrate
fi

if [ $CREATESUPERUSER -eq 1 ]; then
    echo "Creating the superuser..."
    docker compose -f docker-compose.yml -p meteo run --rm backend python manage.py createsuperuser --noinput
fi

if [ $RUNSERVER -eq 1 ]; then
    echo "Running the backend server..."
    docker compose -f docker-compose.yml -p meteo up $FORCE_RECREATE
fi

echo "Script finished. You can pass --help or -h to see the available options."
exit 0
