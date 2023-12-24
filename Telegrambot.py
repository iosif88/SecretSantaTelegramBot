from telebot import types
import telebot

TOKEN = '6575001630:AAGPwRS_gj22_15XBlYns7oxNR95fntdoTQ'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    create_button = types.KeyboardButton(text="Создайте свою комнату и приглосите друзей")
    join_button = types.KeyboardButton(text="Присоединитесь к существующей комнате")
    markup.add(create_button)
    markup.add(join_button)
    bot.send_message(message.chat.id, "Выберите один из вариантов:", reply_markup=markup)


if __name__ == "__main__":
    bot.polling(none_stop=True)
    bot.polling(none_stop=True)