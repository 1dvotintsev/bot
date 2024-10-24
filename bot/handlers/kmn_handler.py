from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from bot.keybords.kmn_keyboards import mode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import random

router = Router()

class GameState(StatesGroup):
    normal = State()
    hard = State()

kmn = ['✊','✌️','🤚']

#перебор всех комбинаций
async def is_win(ans, user):
    if ans == user:
        return None
    
    if ans == kmn[0] and user == kmn[1]:
        return True
    elif ans == kmn[0] and user == kmn[2]:
        return False
    
    if ans == kmn[1] and user == kmn[2]:
        return True
    elif ans == kmn[1] and user == kmn[0]:
        return False
    
    if ans == kmn[2] and user == kmn[0]:
        return True
    elif ans == kmn[2] and user == kmn[1]:
        return False  
    

@router.callback_query(F.data == 'kmn')
async def game(callback: CallbackQuery) -> None:
    await callback.message.answer(text="Отлично, давай сыграем! Выбери сложность",
                                  reply_markup=mode)
    await callback.answer()
    

@router.callback_query(F.data == 'normal')
async def normal_mode(callback: CallbackQuery, state:FSMContext) -> None:
    await callback.message.answer(text="Отлично, отправляй ✊, ✌️ или🤚")
    await state.set_state(GameState.normal)
    await callback.answer()


@router.callback_query(F.data == 'impossible')
async def normal_mode(callback: CallbackQuery, state:FSMContext) -> None:
    await callback.message.answer(text="Смело, отправляй ✊, ✌️ или🤚")
    await state.set_state(GameState.hard)
    await callback.answer()
    

@router.message(GameState.normal)
async def normal_game(msg: Message, state: FSMContext) -> None:
    if msg.text in kmn:
        ans = kmn[random.randint(0,2)]
        win = await is_win(ans, msg.text)
        await msg.answer(text=ans)
        if win == None:
            await msg.answer(text="Ничья! Попробуем еще?")
        else:
            if win:
                await msg.answer(text="Вы проиграли! Попробуем еще?")
            else:
                await msg.answer(text="Вы выиграли! Попробуем еще?")
    else:
        await msg.answer(text="Отправляй только ✊, ✌️ или🤚")
    

@router.message(GameState.hard)
async def normal_game(msg: Message, state: FSMContext) -> None:
    if msg.text in kmn:
        ans = None
        if msg.text == kmn[0]:
            ans = kmn[2]
        if msg.text == kmn[1]:
            ans = kmn[0]
        if msg.text == kmn[2]:
            ans = kmn[1]
        await msg.answer(text=ans)
        await msg.answer(text=f"Вы проиграли! Попробуем еще?")
    else:
        await msg.answer(text="Отправляй только ✊, ✌️ или🤚")   