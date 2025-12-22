import asyncio, logging
from aiogram import Bot, Dispatcher


import handlers
from config import BOT_TOKEN, ALLOWED_USER
from logging_conf import log_start

#hello?

async def main():
    log_start()

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(handlers.monitor_router)
    await bot.send_message(chat_id=ALLOWED_USER, text='Малина запущена')
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())