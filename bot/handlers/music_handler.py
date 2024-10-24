from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from bot.keybords.music_keyboards import blanc
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import random

router = Router()

class GameState(StatesGroup):
    normal = State()
    hard = State() 

#для корректной работы пятого пункта просто сюда подставить все нужные ссылку на музыку и они случайно выдаваться будут
sad_urls = ['url'] 
fun_urls = ['url']
active_urls =['url']    

@router.callback_query(F.data == 'music')
async def game(callback: CallbackQuery) -> None:
    await callback.message.answer(text="Я подберу для тебя музыку. Выбери какое у тебя сейчас настроение",
                                  reply_markup=blanc)
    await callback.answer()
    

@router.callback_query(F.data == 'sad')
async def normal_mode(callback: CallbackQuery) -> None:
    await callback.message.answer(text=f"Мне кажется, тебе подойдет этот трек:\n{sad_urls[random.randint(0,len(sad_urls)-1)]}")
    await callback.answer()


@router.callback_query(F.data == 'fun')
async def normal_mode(callback: CallbackQuery) -> None:
    await callback.message.answer(text=f"Мне кажется, тебе подойдет этот трек:\n{fun_urls[random.randint(0,len(fun_urls)-1)]}")
    await callback.answer()
    

@router.callback_query(F.data == 'active')
async def normal_mode(callback: CallbackQuery) -> None:
    await callback.message.answer(text=f"Мне кажется, тебе подойдет этот трек:\n{active_urls[random.randint(0,len(active_urls)-1)]}")
    await callback.answer()