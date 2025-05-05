import os
import json
import logging
import random
import re
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
)
import drinks  # drinks.yaml подключается через drinks.py

# Загружаем drinks.json
BASE_PATH = os.path.dirname(__file__)
JSON_PATH = os.path.join(BASE_PATH, "drinks.json")

# Читаем как текст, исправляем ошибки с \ и парсим

with open(JSON_PATH, "r", encoding="utf-8") as f:
    content = f.read()
    # Экранируем все одиночные \, которые не являются допустимыми escape-последовательностями
    content = re.sub(r'\\(?![ntr"\\/bfu])', r'\\\\', content)
    DRINKS = json.loads(content)

# Загрузка токена
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# --- Команды ---

async def log_command(update: Update, context: ContextTypes.DEFAULT_TYPE, command_name: str):
    user = update.effective_user
    logger.info(f"User {user.full_name} ({user.id}) called {command_name}")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context, "/start")
    keyboard = [[InlineKeyboardButton("Показать команды 📋", callback_data="show_commands")]]
    await update.message.reply_text(
        "Привет! Я DrinkAdvisorBot 🍹\nНажми кнопку ниже, чтобы увидеть список команд:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context, "/help")
    await update.message.reply_text(
        "/start - Запуск бота\n"
        "/info <название> - Информация о напитке\n"
        "/recipe <название> - Рецепт напитка\n"
        "/cocktails <ингредиент> - Поиск по ингредиенту\n"
        "/random - Случайный напиток\n"
        "/list - Список всех напитков\n"
        "/stop - Остановка бота"
    )


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context, "/info")
    if context.args:
        name = " ".join(context.args)
        await update.message.reply_text(drinks.get_info(name))
    else:
        await update.message.reply_text("Укажи название напитка: /info <название>")


async def recipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context, "/recipe")
    if context.args:
        name = " ".join(context.args)
        await update.message.reply_text(drinks.get_recipe(name))
    else:
        await update.message.reply_text("Укажи название напитка: /recipe <название>")


async def cocktails(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context, "/cocktails")
    if context.args:
        ingredient = " ".join(context.args)
        await update.message.reply_text(drinks.search_by_ingredient(ingredient))
    else:
        await update.message.reply_text("Укажи ингредиент: /cocktails <ингредиент>")


async def random_cocktail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context, "/random")
    all_names = list(drinks.DRINKS.keys())
    choice = random.choice(all_names)
    await update.message.reply_text(f"🎲 Случайный напиток: {choice}\n\n" + drinks.get_info(choice))


async def list_drinks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context, "/list")
    names = list(drinks.DRINKS.keys())
    await update.message.reply_text("📋 Все напитки:\n" + "\n".join(names))


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context, "/stop")
    await update.message.reply_text("Бот остановлен. До встречи! 👋")


# --- Обработка кнопок ---

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "show_commands":
        await query.message.reply_text(
            "/start - Запуск бота\n"
            "/info <название> - Информация о напитке\n"
            "/recipe <название> - Рецепт напитка\n"
            "/cocktails <ингредиент> - Поиск по ингредиенту\n"
            "/random - Случайный напиток\n"
            "/list - Список всех напитков\n"
            "/help - Справка\n"
            "/stop - Остановка бота"
        )


# --- main ---

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("recipe", recipe))
    app.add_handler(CommandHandler("cocktails", cocktails))
    app.add_handler(CommandHandler("random", random_cocktail))
    app.add_handler(CommandHandler("list", list_drinks))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
