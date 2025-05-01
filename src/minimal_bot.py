import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from src.database import Base, engine, get_db
from src.habr_parser import HabrParser
from src.models.news import News
from sqlalchemy.orm import Session

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Загрузка переменных окружения
load_dotenv()

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Создаем клавиатуру
keyboard = [
    ["Start", "News"]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start и кнопки Start"""
    user = update.effective_user
    await update.message.reply_text(
        f"Привет, {user.first_name}! Я бот для получения новостей с Хабра.",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /help"""
    help_text = """
Доступные команды:
/start - Начать работу с ботом
/help - Показать это сообщение

Также вы можете использовать кнопку News для получения новостей.
    """
    await update.message.reply_text(help_text, reply_markup=reply_markup)

def convert_views_to_int(views_str: str) -> int:
    """Преобразует строковое представление количества просмотров в целое число."""
    try:
        # Удаляем все нечисловые символы, кроме десятичной точки
        clean_str = ''.join(c for c in views_str if c.isdigit() or c == '.')
        if 'K' in views_str:
            return int(float(clean_str) * 1000)
        elif 'M' in views_str:
            return int(float(clean_str) * 1000000)
        return int(clean_str)
    except (ValueError, TypeError):
        return 0

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик кнопки News и команды /news"""
    db: Session = next(get_db())
    news = HabrParser.get_news(db)
    
    if not news:
        await update.message.reply_text(
            "К сожалению, новых новостей пока нет. Попробуйте позже.",
            reply_markup=reply_markup
        )
        return
    
    for item in news:
        # Формируем сообщение с информацией о новости
        message = (
            f"📰 {item['title']}\n\n"
            f"👤 Автор: {item['author']}\n"
            f"👁 Просмотров: {item['views']}\n"
            f"🔗 {item['link']}"
        )
        
        # Сохраняем новость в базу данных
        db_news = News(
            title=item['title'],
            link=item['link'],
            author=item['author'],
            views=convert_views_to_int(item['views']),
            image_url=item['image_url']
        )
        db.add(db_news)
        
        # Отправляем новость
        if item['image_url']:
            # Если есть изображение, отправляем его с подписью
            await update.message.reply_photo(
                photo=item['image_url'],
                caption=message,
                parse_mode='HTML',
                reply_markup=reply_markup
            )
        else:
            # Если изображения нет, отправляем только текст
            await update.message.reply_text(
                message,
                parse_mode='HTML',
                reply_markup=reply_markup
            )
    
    db.commit()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик текстовых сообщений"""
    text = update.message.text
    if text == "News":
        await news(update, context)
    elif text == "Start":
        await start(update, context)
    else:
        await update.message.reply_text(
            "Используйте кнопки или команды для взаимодействия с ботом.",
            reply_markup=reply_markup
        )

def main() -> None:
    """Запуск бота"""
    # Создаем приложение
    application = Application.builder().token(os.getenv("BOT_TOKEN")).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("news", news))  # Добавляем обработчик команды /news
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main() 