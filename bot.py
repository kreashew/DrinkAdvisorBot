import os
import logging
from dotenv import load_dotenv
from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

from drinks import get_info, get_recipe, get_by_ingredient, get_random, get_all_drinks

# Загрузка токена
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# Лог команды
async def log_command(update: Update, context: ContextTypes.DEFAULT_TYPE, command_name: str):
    user = update.effective_user
    logger.info(f"Пользователь {user.full_name} ({user.id}) ввёл команду: {command_name}")


# /start с инлайн-кнопкой
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context, "/start")
    keyboard = [[InlineKeyboardButton("Показать команды 📋", callback_data="show_commands")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! Я DrinkAdvisorBot 🍹\nНажми кнопку ниже, чтобы увидеть список команд:",
        reply_markup=reply_markup
    )


# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context, "/help")
    await update.message.reply_text(
        "/start - Запуск бота\n"
        "/info <название> - Информация о напитке\n"
        "/recipe <название> - Рецепт напитка\n"
        "/cocktails <ингредиент> - Коктейли по ингредиенту\n"
        "/random - Случайный коктейль\n"
        "/list - Показать все доступные напитки\n"
        "/stop - Остановка бота"
    )


# /info
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context, "/info")
    if context.args:
        drink = ' '.join(context.args)
        await update.message.reply_text(get_info(drink))
    else:
        await update.message.reply_text("Укажи название напитка: /info <название>")


# /recipe
async def recipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context, "/recipe")
    if context.args:
        drink = ' '.join(context.args)
        await update.message.reply_text(get_recipe(drink))
    else:
        await update.message.reply_text("Укажи название: /recipe <название>")


# /cocktails
async def cocktails(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context, "/cocktails")
    if context.args:
        ingredient = ' '.join(context.args)
        await update.message.reply_text(get_by_ingredient(ingredient))
    else:
        await update.message.reply_text("Укажи ингредиент: /cocktails <ингредиент>")


# /random
async def random_cocktail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context, "/random")
    await update.message.reply_text(get_random())


# /list
async def list_drinks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context, "/list")
    await update.message.reply_text(get_all_drinks())


# /stop
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context, "/stop")
    await update.message.reply_text("Бот остановлен. До встречи! 👋")


# Обработчик инлайн-кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "show_commands":
        logger.info(f"Пользователь нажал кнопку 'Показать команды' — id: {query.from_user.id}")
        await query.message.reply_text(
            "/start - Запуск бота\n"
            "/info <название> - Информация о напитке\n"
            "/recipe <название> - Рецепт напитка\n"
            "/cocktails <ингредиент> - Коктейли по ингредиенту\n"
            "/random - Случайный коктейль\n"
            "/list - Показать все доступные напитки\n"
            "/stop - Остановка бота"
        )


# Точка входа
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("recipe", recipe))
    app.add_handler(CommandHandler("cocktails", cocktails))
    app.add_handler(CommandHandler("random", random_cocktail))
    app.add_handler(CommandHandler("list", list_drinks))
    app.add_handler(CommandHandler("stop", stop))

    # Инлайн-кнопка
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
