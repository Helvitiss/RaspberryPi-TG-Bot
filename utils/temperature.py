import asyncio, logging

from aiogram import Bot
from psutil import sensors_temperatures

def get_cpu_temp() -> float:
    temp = sensors_temperatures().get('cpu_thermal')[0].current
    return temp


async def temp_watcher(
        bot: Bot,
        admin_id: int,
        threshold: float = 70.0,
        interval: int = 60):
    """Проверка в температуры в фоне и уведомление при превышении трешхолда"""
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

if __name__ == '__main__':
    print(get_cpu_temp())