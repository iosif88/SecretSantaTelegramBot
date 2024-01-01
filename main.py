from telebot import TeleBot
from handlers import register_handlers
from config import TOKEN

bot = TeleBot(TOKEN)

if __name__ == "__main__":
    register_handlers(bot)
    bot.polling(none_stop=True)