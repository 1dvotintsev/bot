import requests
from aiogram import Router, F
from aiogram.types import CallbackQuery
from bot.keybords.joke_keybords import repeate
from config import JOKE_API_URL

router = Router()


@router.callback_query(F.data == 'joke')
async def send_joke(callback: CallbackQuery):
    try:
        response = requests.get(JOKE_API_URL)

        if response.status_code == 200:
            # Парсим JSON-ответ
            data = response.json()

            # Извлекаем анекдот из данных
            joke = data.get("item", {}).get("text", "Не удалось получить анекдот.")
        else:
            joke = "Не удалось получить анекдот. Попробуйте позже."
    except:
        joke = "Не удалось получить анекдот"

    await callback.message.answer(text=joke,
                                  reply_markup=repeate)
    await callback.answer()
