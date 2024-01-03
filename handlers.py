from telebot import types
from text import first_presentation_bot_capabilities
from db import execute_query, connect_to_database
from kb import create_keyboard_markup

def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        query_insert_user = get_user_info(message)
        execute_query(query_insert_user,message.from_user.id)

        markup = create_keyboard_markup()
        bot.send_message(message.chat.id, first_presentation_bot_capabilities, reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == "Создайте свою комнату и приглосите друзей")
    def create_room(message):
        bot.send_message(message.chat.id, "Напишите уникальное имя для комнаты.")

    @bot.message_handler(func=lambda message: message.text == "Присоединитесь к существующей комнате")
    def join_room(message):
        bot.send_message(message.chat.id, "Введите уникальный идентификатор комнаты,к который вы хотите подключиться .")

    # Добавьте другие обработчики, как необходимо
        
def get_user_id(message):
    user_telegram_id = message.from_user.id
    return user_telegram_id

def get_user_info(message):
    user_name = message.from_user.first_name
    user_telegram_id = get_user_id(message)
    query = f"""
    INSERT INTO users (first_name, user_telegram_id) 
    VALUES ('{user_name}', {user_telegram_id});"""
    return query
