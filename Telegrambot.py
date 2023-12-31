from telebot import types
import telebot
from database_operations import connect_to_database, execute_query
from bot_text_response import first_presentation_bot_capabilities 

TOKEN = '6575001630:AAGPwRS_gj22_15XBlYns7oxNR95fntdoTQ'
bot = telebot.TeleBot(TOKEN)

def main():
    @bot.message_handler(commands=['start'])
    def start(message):
        query_insert_user = get_user_info(message)
        execute_query(query_insert_user)

        markup = create_keyboard_markup()
        bot.send_message(message.chat.id,first_presentation_bot_capabilities, reply_markup=markup)

    def get_user_info(message):
            user_name = message.from_user.first_name
            user_telegram_id = message.from_user.id
            query = f"""INSERT INTO users (first_name, user_telegram_id) VALUES ('{user_name}', {user_telegram_id});"""
            return query
    
    def create_keyboard_markup():
        markup = types.ReplyKeyboardMarkup()
        create_button = types.KeyboardButton(text="Создайте свою комнату и приглосите друзей")
        join_button = types.KeyboardButton(text="Присоединитесь к существующей комнате")
        markup.add(create_button)
        markup.add(join_button)
        return markup
    
    @bot.message_handler(func=lambda message: message.text == "Создайте свою комнату и приглосите друзей")
    def create_room(message):
        bot.send_message(message.chat.id, "Напишите уникальное имя для комнаты.")

    if __name__ == "__main__":
        bot.polling(none_stop=True)

if __name__ == "__main__":
    main()
