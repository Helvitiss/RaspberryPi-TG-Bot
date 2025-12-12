import asyncio, logging
from aiogram import Bot, Dispatcher


import handlers
from config import BOT_TOKEN
from logging_conf import setup_logging



async def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(handlers.monitor_router)

    logger.info('Бот запущен') 
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())