import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os
from drinks import get_info, get_recipe, get_by_ingredient, get_random  # ✅ подключение

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я DrinkAdvisorBot 🍹\n"
        "Напиши /help, чтобы узнать, что я умею."
    )


# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Запуск бота\n"
        "/info <название> - Информация о напитке\n"
        "/recipe <название> - Рецепт напитка\n"
        "/cocktails <ингредиент> - Коктейли по ингредиенту\n"
        "/random - Случайный коктейль\n"
        "/stop - Остановка бота"
    )


# /info
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        drink = ' '.join(context.args)
        await update.message.reply_text(get_info(drink))
    else:
        await update.message.reply_text("Укажи название напитка: /info <название>")


# /recipe
async def recipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        drink = ' '.join(context.args)
        await update.message.reply_text(get_recipe(drink))
    else:
        await update.message.reply_text("Укажи название: /recipe <название>")


# /cocktails
async def cocktails(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        ingredient = ' '.join(context.args)
        await update.message.reply_text(get_by_ingredient(ingredient))
    else:
        await update.message.reply_text("Укажи ингредиент: /cocktails <ингредиент>")


# /random
async def random_cocktail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_random())


# /stop
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
    app.add_handler(CommandHandler("stop", stop))

    print("🤖 Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
