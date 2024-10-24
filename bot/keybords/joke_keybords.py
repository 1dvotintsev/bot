from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


repeate = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Еще анекдот!', callback_data='joke')],
])