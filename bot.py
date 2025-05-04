import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

load_dotenv()  # Загружаем токен из .env

TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я DrinkAdvisorBot 🍹\n"
        "Напиши /help, чтобы узнать, что я умею."
    )


# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Запуск бота\n"
        "/info <название> - Инфо о напитке\n"
        "/recipe <название> - Рецепт напитка\n"
        "/cocktails <ингредиент> - Коктейли по ингредиенту\n"
        "/random - Случайный коктейль\n"
        "/alternative <название> - Безалкогольная версия\n"
        "/stop - Остановка бота"
    )


# Команда /info
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        drink = ' '.join(context.args)
        # Заглушка, тут будет логика
        await update.message.reply_text(f"Информация о напитке: {drink}")
    else:
        await update.message.reply_text("Укажи название напитка: /info <название>")


# Команда /recipe
async def recipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        drink = ' '.join(context.args)
        await update.message.reply_text(f"Рецепт напитка: {drink}")
    else:
        await update.message.reply_text("Укажи название: /recipe <название>")


# Команда /cocktails
async def cocktails(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        ingredient = ' '.join(context.args)
        await update.message.reply_text(f"Коктейли с ингредиентом: {ingredient}")
    else:
        await update.message.reply_text("Укажи ингредиент: /cocktails <ингредиент>")


# Команда /random
async def random_cocktail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎲 Случайный коктейль: Mojito (пример)")


# Команда /alternative
async def alternative(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        original = ' '.join(context.args)
        await update.message.reply_text(f"Безалкогольная версия для: {original}")
    else:
        await update.message.reply_text("Укажи коктейль: /alternative <название>")


# Команда /stop
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот остановлен. До встречи! 👋")


# Основной запуск
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("recipe", recipe))
    app.add_handler(CommandHandler("cocktails", cocktails))
    app.add_handler(CommandHandler("random", random_cocktail))
    app.add_handler(CommandHandler("alternative", alternative))
    app.add_handler(CommandHandler("stop", stop))

    print("🤖 Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
