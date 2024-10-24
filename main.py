import asyncio

from config import TOKEN

from aiogram import Bot, Dispatcher

from bot.handlers.user_handlers import router as user_router
from bot.handlers.notifications_handlers import router as note_router
from bot.handlers.kmn_handler import router as kmn_router
from bot.handlers.wheather_handlers import router as wheather_router
from bot.handlers.joke_handler import router as joke_router
from bot.handlers.music_handler import router as music_router


bot = Bot(token = TOKEN)
dp = Dispatcher()


async def main() -> None:
    dp.include_router(user_router)
    dp.include_router(note_router)
    dp.include_router(kmn_router)
    dp.include_router(wheather_router)
    dp.include_router(joke_router)
    dp.include_router(music_router)
    
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
            print(f"Error: {e}")