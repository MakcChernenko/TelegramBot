from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привіт 👋")],
        [KeyboardButton(text="Допомога ❓")]
    ],
    resize_keyboard=True
)
