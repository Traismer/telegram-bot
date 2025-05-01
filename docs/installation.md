# Установка и запуск

## Локальная разработка

1. Установите pipenv, если еще не установлен:
```bash
pip install pipenv
```

2. Установите зависимости и создайте виртуальное окружение:
```bash
pipenv install
```

3. Активируйте виртуальное окружение:
```bash
pipenv shell
```

4. Создайте файл `.env` с необходимыми переменными окружения:
```bash
# Скопируйте шаблон конфигурации
cp .env.example .env

# Отредактируйте файл .env, заменив значения на свои
nano .env
```

Файл `.env` должен содержать следующие переменные:
```bash
# Telegram Bot Configuration
BOT_TOKEN=your_bot_token_here
BOT_USERNAME=your_bot_username_here
ADMIN_ID=your_admin_id_here

# Database Configuration
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=telegram_bot_db

# Timezone
TZ=Europe/Moscow
```

5. Запустите бота:
```bash
python src/minimal_bot.py
```

## Полезные команды pipenv

- `pipenv shell` - активировать виртуальное окружение
- `pipenv install` - установить зависимости
- `pipenv install --dev` - установить зависимости для разработки
- `pipenv install <package>` - установить новый пакет
- `pipenv uninstall <package>` - удалить пакет
- `pipenv graph` - показать дерево зависимостей
- `exit` - выйти из виртуального окружения 