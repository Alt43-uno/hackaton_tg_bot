from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def main_keyboard():
    kb = [
        [KeyboardButton(text='🏷 Получить номер в очереди')]
    ]

    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Выберите вариант из меню")
    return keyboard

