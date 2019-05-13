#!/usr/bin/env bash

# This will fail if postgresql is not set up, and configured to allow database and user creation
# For reference on peer auth failure: https://stackoverflow.com/a/18664239

echo "Creating new User and Database"
psql -U postgres -c "CREATE USER djangodnd WITH PASSWORD 'djangodnd';"
psql -U postgres -c "ALTER USER djangodnd CREATEDB;"
psql -U postgres -c "CREATE DATABASE djangodnd OWNER djangodnd;"