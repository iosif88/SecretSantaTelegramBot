from telebot import types

def create_keyboard_markup():
    markup = types.ReplyKeyboardMarkup()
    create_button = types.KeyboardButton(text="Создайте свою комнату и приглосите друзей")
    join_button = types.KeyboardButton(text="Присоединитесь к существующей комнате")
    markup.add(create_button)
    markup.add(join_button)
    return markup