# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем pipenv
RUN pip install pipenv

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY Pipfile Pipfile.lock ./

# Устанавливаем зависимости
RUN pipenv install --deploy --system

# Копируем исходный код и скрипт инициализации
COPY src/ ./src/
COPY init-db.sh .

# Устанавливаем переменную PYTHONPATH
ENV PYTHONPATH=/app

# Запускаем бота
CMD ["python", "src/minimal_bot.py"]