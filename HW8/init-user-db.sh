#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    create database test_db;
    create user test with encrypted password '1111';
    grant all privileges on database test_db to test;
EOSQL
