from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Поставить напоминание", callback_data='set_notification')],
    [InlineKeyboardButton(text="Сыграть КМН", callback_data='kmn')],
    [InlineKeyboardButton(text="Узнать погоду", callback_data='wheather')],
    [InlineKeyboardButton(text="Рассказать анекдот", callback_data='joke')],
    [InlineKeyboardButton(text="Подобрать музыку", callback_data='music')],   
])