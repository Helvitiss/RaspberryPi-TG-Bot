import asyncio, subprocess, logging

from aiogram import Bot
from aiogram.types import Update


def get_cpu_temp() -> float:
    result = subprocess.run(["vcgencmd", "measure_temp"],
                            capture_output=True, text=True)

    output = result.stdout
    temp_str = output.split('=')[1]
    temp = float(temp_str.replace('C', ''))

    return temp


async def temp_watcher(
        bot: Bot,
        admin_id: int,
        threshold: float = 70.0,
        interval: int = 60):
    """Проверка в температуры в фоне и уведомление при превышение трешхолда"""
    notified = False

    while True:
        try:
            temp = get_cpu_temp()
            logging.info(f'Температура: {temp}C')

            if temp >= threshold and not notified:
                await bot.send_message(admin_id, f'ВНИМАНИЕ!\nТемпература CPU: {temp}')
                logging.warning(f'Превышена температура CPU: {temp}C')
                notified = True
            else:
                notified = False

        except Exception as e:
            logging.error(f"Ошибка проверки температуры {e}")

        await asyncio.sleep(interval)

