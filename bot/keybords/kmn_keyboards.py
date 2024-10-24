from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


mode = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Normal', callback_data='normal'), InlineKeyboardButton(text='Impossible', callback_data='impossible')]
])