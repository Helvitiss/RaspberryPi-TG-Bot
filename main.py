import asyncio
from aiogram import Bot, Dispatcher

import handlers
from core.config import BOT_TOKEN
from core.startup import startup

async def main():

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(handlers.monitor_router)
    dp.include_router(handlers.control_router)

    await startup(bot)


    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())