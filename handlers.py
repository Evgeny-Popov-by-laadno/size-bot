from bot.keyboards import get_main_menu
from bot.utils import calculate_size

user_data = {}

def register_handlers(bot):
    
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        user_id = message.from_user.id
        if user_id in user_data:
            del user_data[user_id]
            
        bot.send_message(
            message.chat.id, 
            "Добро пожаловать в бот для подбора одежды BRANDORA https://t.me/branddorachat ! 👋\nЯ помогу определить размер и проверить его наличие. \nP.S Функция проверки наличия в разработке"
        )
        bot.send_message(
            message.chat.id, 
            "Пожалуйста, выберите категорию одежды:",
            reply_markup=get_main_menu()
        )

    # Обработчик кнопки "Проверить наличие"
    @bot.message_handler(func=lambda message: message.text == "🔄 Проверить наличие")
    def check_availability(message):
        bot.send_message(
            message.chat.id,
            "куда ты жмешь епта, написано же в разработке"
        )

    @bot.message_handler(func=lambda message: message.text in ["Футболки", "Шорты", "Штаны", "Кофты", "Верхняя одежда"])
    def category_chosen(message):
        user_id = message.from_user.id
        user_data[user_id] = {"category": message.text}
        bot.send_message(
            message.chat.id, 
            f"Вы выбрали категорию: <b>{message.text}</b>\n\nВведите ваш <b>рост</b> в см (например, 178):",
            parse_mode="HTML"
        )

    @bot.message_handler(func=lambda message: message.from_user.id in user_data and "height" not in user_data[message.from_user.id])
    def get_height(message):
        user_id = message.from_user.id
        try:
            height = int(message.text)
            if height < 100 or height > 220:
                bot.reply_to(message, "Введите реальный рост (от 100 до 220 см).")
                return
            user_data[user_id]["height"] = height
            bot.send_message(message.chat.id, "Теперь введите ваш <b>вес</b> в кг (например, 70):", parse_mode="HTML")
        except ValueError:
            bot.reply_to(message, "Рост должен быть числом.")

    @bot.message_handler(func=lambda message: message.from_user.id in user_data and "weight" not in user_data[message.from_user.id])
    def get_weight_and_result(message):
        user_id = message.from_user.id
        try:
            weight = int(message.text)
            if weight < 30 or weight > 200:
                bot.reply_to(message, "Введите реальный вес (от 30 до 200 кг).")
                return
            
            user_data[user_id]["weight"] = weight
            category = user_data[user_id]["category"]
            height = user_data[user_id]["height"]
            size = calculate_size(category, height, weight)
            
            response = (
                f"📊 <b>Результат подбора:</b>\n\n"
                f"Категория: {category}\n"
                f"Рост: {height} см\n"
                f"Вес: {weight} кг\n\n"
                f"👉 <b>Рекомендуемый размер: {size}</b>"
            )
            
            bot.send_message(message.chat.id, response, parse_mode="HTML")
            bot.send_message(
                message.chat.id, 
                "Хотите подобрать что-то ещё? Выберите категорию:", 
                reply_markup=get_main_menu()
            )
            
            del user_data[user_id]
            
        except ValueError:
            bot.reply_to(message, "Вес должен быть числом.")