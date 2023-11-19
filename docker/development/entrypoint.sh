#! /bin/bash

mkdir -p logs/

bash /wait-for-it.sh database:5432 --timeout=30 -- echo "Postgres is up"

exec "$@"
