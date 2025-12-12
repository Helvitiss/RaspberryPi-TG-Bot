import asyncio, logging
from aiogram import Bot, Dispatcher


import handlers
from config import BOT_TOKEN
from logging_conf import log_start



async def main():
    log_start()

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(handlers.monitor_router)

    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())