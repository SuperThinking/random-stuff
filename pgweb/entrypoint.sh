#!/bin/sh
# wait-for-it.sh


until nc -z $HOST 5432; do
  >&2 echo "Postgres - $HOST host is unavailable - sleeping"
  sleep 1
done

echo "Postgres - $HOST is up. Running.."

"$@"
