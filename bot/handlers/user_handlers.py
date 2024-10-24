from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from bot.keybords.user_keybords import main_menu
from aiogram.fsm.context import FSMContext

router = Router()

reminders = []

@router.message(CommandStart())
async def cmd_start(msg: Message, state: FSMContext) -> None:
    await state.clear()
    await msg.answer(text=f"Привет, {msg.from_user.first_name}, я могу помочь тебе со следующими функциями: ",
                     reply_markup=main_menu)


