#!/bin/bash

# Ожидание готовности PostgreSQL
echo "Ожидание готовности PostgreSQL..."
while ! PGPASSWORD=postgres pg_isready -h postgres -p 5432 -U postgres; do
    sleep 1
done

# Создание базы данных
echo "Создание базы данных..."
PGPASSWORD=postgres psql -h postgres -U postgres -c "CREATE DATABASE telegram_bot_db;"

echo "Инициализация базы данных завершена!" 