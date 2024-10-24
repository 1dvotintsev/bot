import asyncio
from datetime import datetime
import pytz
from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config import TOKEN

router = Router()


bot = Bot(token=TOKEN)


class NoteState(StatesGroup):
    set_text = State()
    set_time = State()


#вычисление задержки до даты отправки
async def schedule_reminder(chat_id: int, send_time: datetime, text: str):
    now = datetime.now(pytz.utc)
    delay = (send_time - now).total_seconds()
    if delay > 0:
        await asyncio.sleep(delay)  # Ожидание до запланированного времени
        await bot.send_message(chat_id, 'Напоминание: '+text)


@router.callback_query(F.data == 'set_notification')
async def set_note(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer("Введите текст напоминания:")
    await state.set_state(NoteState.set_text)
    await callback.answer()


@router.message(NoteState.set_text)
async def get_description(msg: Message, state: FSMContext) -> None:
    await state.update_data(text=msg.text)
    await msg.answer(text="Когда отправить напоминание? Ответьте в формате: YYYY-MM-DD HH:MM")
    await state.set_state(NoteState.set_time)


@router.message(NoteState.set_time)
async def cmd_remind(msg: Message, state: FSMContext) -> None:
    try:
        data = await state.get_data()
        text = data['text']

        schedule_time_str = msg.text
        # Преобразуем строку в объект datetime
        send_time = datetime.strptime(schedule_time_str, "%Y-%m-%d %H:%M")

        # Устанавливаем часовой пояс (Москва)
        timezone = pytz.timezone('Europe/Moscow')
        send_time = timezone.localize(send_time)

        await msg.answer(f"Напоминание '{text}' запланировано на {send_time}.")
        # Запускаем фоновую задачу
        asyncio.create_task(schedule_reminder(msg.chat.id, send_time, text))

    except ValueError:
        await msg.answer("Неверный формат даты. Пожалуйста, введите дату в формате: YYYY-MM-DD HH:MM")

    finally:
        await state.clear()  # Сброс состояния после завершения
