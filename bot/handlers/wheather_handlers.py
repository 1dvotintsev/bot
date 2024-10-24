import requests
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from config import WTOKEN, WEATHER_API_URL
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class Wheather(StatesGroup):
    input = State()

router = Router()

Wheather()

@router.callback_query(F.data == 'wheather')
async def start_command(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите название города, чтобы получить прогноз погоды.")
    await callback.answer()
    await state.set_state(Wheather.input)


@router.message(Wheather.input )
async def get_weather(msg: Message, state: FSMContext ):
    city = msg.text.strip()
    params = {
        'key': WTOKEN,
        'q': city,
        'aqi': 'no'  # Запрос без информации о качестве воздуха
    }
    
    response = requests.get(WEATHER_API_URL, params=params)
    data = response.json()
    
    #сохраняем необходимые данные
    if response.status_code == 200:
        location = data['location']['name']
        region = data['location']['region']
        country = data['location']['country']
        temperature = data['current']['temp_c']
        weather_description = data['current']['condition']['text']
        humidity = data['current']['humidity']
        wind_speed = data['current']['wind_kph']

        weather_report = (
            f"Погода в городе {location}, {region}, {country}:\n"
            f"Температура: {temperature}°C\n"
            f"Описание: {weather_description}\n"
            f"Влажность: {humidity}%\n"
            f"Скорость ветра: {wind_speed} км/ч"
        )
        await msg.answer(weather_report)
        await state.clear()
    else:
        await msg.answer(f"Не удалось получить данные о погоде для города '{city}'. Проверьте правильность названия.")
