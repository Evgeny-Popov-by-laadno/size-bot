from telebot import types

def get_main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        types.KeyboardButton("Футболки"),
        types.KeyboardButton("Шорты"),
        types.KeyboardButton("Штаны"),
        types.KeyboardButton("Кофты"),
        types.KeyboardButton("Верхняя одежда"),
        types.KeyboardButton("🔄 Проверить наличие")  # Новая кнопка
    )
    return keyboard