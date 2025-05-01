# Разработка

## Структура проекта

```
.
├── src/
│   ├── minimal_bot.py    # Основной файл бота
│   ├── database.py       # Настройки базы данных
│   ├── habr_parser.py    # Парсер новостей с Хабра
│   └── models/
│       └── news.py       # Модель новости
├── Pipfile               # Зависимости проекта
├── Pipfile.lock         # Закрепленные версии зависимостей
├── Dockerfile           # Конфигурация Docker
├── docker-compose.yml   # Конфигурация Docker Compose
└── docs/                # Документация
```

## Требования

- Python 3.10 или выше
- PostgreSQL 15 или выше
- pipenv для управления зависимостями

## Зависимости

Основные зависимости:
- python-telegram-bot==20.7
- python-dotenv==1.0.0
- SQLAlchemy==2.0.27
- psycopg2-binary==2.9.9
- beautifulsoup4==4.12.3
- requests==2.31.0

Зависимости для разработки:
- pytest==7.4.3
- pytest-asyncio==0.21.1
- pytest-cov==4.1.0 