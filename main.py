import telebot
from handlers import register_handlers
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

register_handlers(bot)

if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()
