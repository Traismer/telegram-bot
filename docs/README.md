# Telegram Bot для новостей Хабра

Бот для получения и отправки новостей с Хабра в Telegram.

## Содержание

- [Установка и запуск](installation.md)
- [Функциональность](features.md)
- [Разработка](development.md)
- [Docker](docker.md)
- [Тестирование](testing.md)
- [Лицензия](license.md)

## Основные возможности

- Получение новостей с Хабра
- Отправка новостей в Telegram
- Сохранение новостей в базу данных
- Удобный интерфейс с кнопками

## Технологии

- Python 3.11
- Telegram Bot API
- PostgreSQL
- SQLAlchemy
- Docker
- pytest для тестирования

## Разработка

### Установка зависимостей

```bash
pipenv install
```

### Запуск в режиме разработки

```bash
pipenv shell
python src/minimal_bot.py
```

### Тестирование

```bash
# Установка зависимостей для тестирования
pipenv install --dev

# Запуск тестов
pytest

# Запуск тестов с покрытием
pytest --cov=src
```

Подробнее о тестировании в [документации](testing.md).

## Docker

```bash
# Сборка и запуск
docker-compose up -d

# Запуск тестов в контейнере
docker-compose exec bot pytest
```

## Лицензия

MIT License. Подробнее в [LICENSE](license.md). 