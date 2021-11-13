#!/bin/sh

if [ "$DATABASE" = "mysql" ]
then
    echo "Waiting for mysql..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "mysql started"
fi

python3 manage.py flush --no-input
python3 manage.py migrate
pipenv install

exec "$@"