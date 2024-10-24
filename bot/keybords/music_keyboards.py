from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


blanc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Грустное', callback_data='sad')],
    [InlineKeyboardButton(text='Веселое', callback_data='fun')],
    [InlineKeyboardButton(text='Бодрое', callback_data='active')]
])