#!/usr/bin/env bash

echo "Creating new User and Database"
psql -U postgres -c "CREATE USER djangodnd WITH PASSWORD 'djangodnd';"
psql -U postgres -c "ALTER USER djangodnd CREATEDB;"
psql -U postgres -c "CREATE DATABASE djangodnd OWNER djangodnd;"