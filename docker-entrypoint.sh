#!/bin/bash

function test_postgresql {
  pg_isready -h "${db_server}" -d "${db}" -U "${db_user}"
  echo $db_user
  echo $db_server
  echo $db
}

cd /code

echo DATABASE_URL: $DATABASE_URL
regex="^postgres:\/\/([^:]+)(:(.+))?@(.+)(:\d{4})?\/(.+)$"
if [[ $DATABASE_URL =~ $regex ]]
then
  db_user="${BASH_REMATCH[1]}"
  db_server="${BASH_REMATCH[4]}"
  db="${BASH_REMATCH[6]}"
else
  >&2 echo "DATABASE_URL is not valid"
  exit 1
fi

# wait for postgres to be ready
count=0
until ( test_postgresql ) do
  ((count++))
  if [ ${count} -gt 45 ]
  then
    >&2 echo "Services didn't become ready in time"
    exit 1
  fi
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
>&2 echo "Postgres ready - continuing"

python manage.py collectstatic --noinput
python manage.py migrate                  # Apply database migrations

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn excellajobs.wsgi:application \
 --name excellajobs \
 --bind 0.0.0.0:$PORT \
 --workers 3 \
 --reload \
 "$@"