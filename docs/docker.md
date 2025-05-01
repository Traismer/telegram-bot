# Docker

## Запуск в Docker

1. Убедитесь, что у вас установлен Docker и Docker Compose

2. Создайте файл `.env` с необходимыми переменными окружения:
```bash
BOT_TOKEN=your_bot_token_here
BOT_USERNAME=your_bot_username_here
ADMIN_ID=your_admin_id_here
```

3. Запустите контейнеры:
```bash
docker-compose up --build
```

4. Для остановки:
```bash
docker-compose down
```

## Структура Docker

Проект состоит из двух контейнеров:

1. `postgres` - база данных PostgreSQL
   - Версия: 15
   - Порт: 5432
   - Данные сохраняются в томе `postgres_data`

2. `bot` - сервис бота
   - Основан на Python 3.11
   - Использует pipenv для управления зависимостями
   - Автоматически инициализирует базу данных при запуске

## Переменные окружения

- `BOT_TOKEN` - токен Telegram бота
- `BOT_USERNAME` - имя пользователя бота
- `ADMIN_ID` - ID администратора
- `POSTGRES_USER` - пользователь PostgreSQL
- `POSTGRES_PASSWORD` - пароль PostgreSQL
- `POSTGRES_HOST` - хост PostgreSQL
- `POSTGRES_PORT` - порт PostgreSQL
- `POSTGRES_DB` - имя базы данных 