# Тестирование

## Обзор

Проект использует pytest для тестирования. Тесты разделены на несколько категорий:
- Тесты команд бота
- Тесты парсера новостей
- Тесты базы данных

## Структура тестов

```
tests/
├── conftest.py          # Конфигурация тестов
├── test_bot_commands.py # Тесты команд бота
└── test_habr_parser.py  # Тесты парсера новостей
```

## Запуск тестов

### Локальная разработка

1. Убедитесь, что у вас установлены все зависимости:
```bash
pipenv install --dev
```

2. Запустите тесты:
```bash
pytest
```

3. Для запуска конкретного теста:
```bash
pytest tests/test_bot_commands.py
```

4. Для запуска с подробным выводом:
```bash
pytest -v
```

### В Docker

1. Соберите и запустите контейнер:
```bash
docker-compose up -d
```

2. Запустите тесты:
```bash
docker-compose exec bot pytest
```

3. Для запуска тестов с покрытием:
```bash
docker-compose exec bot pytest --cov=src
```

## Фикстуры

### mock_update
Создает мок объекта Update для тестирования обработчиков бота:
```python
@pytest.fixture
def mock_update():
    update = MagicMock(spec=Update)
    update.message = MagicMock(spec=Message)
    update.message.reply_text = AsyncMock()
    update.message.reply_photo = AsyncMock()
    update.effective_user = MagicMock(spec=User)
    update.effective_user.first_name = "Test User"
    return update
```

### mock_context
Создает мок объекта Context для тестирования обработчиков бота:
```python
@pytest.fixture
def mock_context():
    context = MagicMock(spec=ContextTypes.DEFAULT_TYPE)
    return context
```

### db_session
Создает тестовую сессию базы данных:
```python
@pytest.fixture
def db_session(db):
    connection = db.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()
```

## Тесты команд бота

### test_start_command
Тестирует команду `/start`:
- Проверяет отправку приветственного сообщения
- Проверяет наличие имени пользователя в сообщении

### test_help_command
Тестирует команду `/help`:
- Проверяет наличие всех команд в справке
- Проверяет форматирование сообщения

### test_handle_message_start
Тестирует обработку кнопки "Start":
- Проверяет отправку приветственного сообщения
- Проверяет корректность ответа

### test_handle_message_news
Тестирует обработку кнопки "News":
- Проверяет попытку отправки новостей
- Проверяет формат ответа

### test_handle_message_unknown
Тестирует обработку неизвестных сообщений:
- Проверяет отправку подсказки
- Проверяет формат ответа

## Тесты парсера новостей

### test_get_news
Тестирует получение новостей:
- Проверяет парсинг HTML
- Проверяет корректность данных
- Проверяет конвертацию значений

### test_save_news
Тестирует сохранение новостей:
- Проверяет добавление в базу данных
- Проверяет коммит транзакции

### test_get_news_empty
Тестирует обработку пустого ответа:
- Проверяет корректную обработку отсутствия новостей

### test_get_news_error
Тестирует обработку ошибок:
- Проверяет обработку исключений
- Проверяет возврат пустого списка при ошибке

## Тестирование базы данных

Тесты используют SQLite в памяти для изоляции:
- Каждый тест работает в своей транзакции
- После теста транзакция откатывается
- База данных создается и удаляется для каждого теста

## Советы по написанию тестов

1. Используйте фикстуры для общих объектов
2. Изолируйте тесты друг от друга
3. Проверяйте как успешные, так и ошибочные сценарии
4. Используйте моки для внешних зависимостей
5. Пишите понятные и информативные сообщения об ошибках

## Покрытие кода

Для проверки покрытия кода тестами:
```bash
pytest --cov=src
```

Для генерации отчета:
```bash
pytest --cov=src --cov-report=html
```

## Запуск тестов в CI/CD

Тесты автоматически запускаются при каждом пуше в репозиторий. Для запуска тестов в CI/CD:

1. Убедитесь, что все зависимости установлены:
```bash
pipenv install --dev
```

2. Запустите тесты:
```bash
pytest
```

3. Проверьте покрытие кода:
```bash
pytest --cov=src --cov-report=term-missing
``` 