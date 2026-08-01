import asyncio

from settings.config import TOKEN
from handlers import router

from aiogram import Bot, Dispatcher


bot = Bot(token=TOKEN)
db = Dispatcher()

db.include_router(router)

async def main():
    await db.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")