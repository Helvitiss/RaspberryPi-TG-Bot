import asyncio
import logging

from typing import Callable, List
from aiogram import Bot


from dictionary import cpu_alert, ram_alert, disk_alert, temp_alert
from utils.metrics import get_cpu_percentage, get_cpu_temp, get_ram_percentage, get_storage_percentage

logger = logging.getLogger(__name__)

async def startup_notification(bot: Bot, admin_ids: List[int]):
    """Отправляет по определенному айди сообщение о запуске системы"""

    try:
        for admin_id in admin_ids:
            await bot.send_message(admin_id, 'Система запущена')
        logger.info('Уведомление о запуске системы отправлено ')
    except Exception as e:
        logger.exception(e)




async def setup_all_watchers(bot: Bot, admin_id: List[int]):
    """Функция, которая запускает все процессы мониторинга Малины"""

    #Мониторинг нагруженности процессора
    asyncio.create_task(watcher(name='CPU',
                                get_value=get_cpu_percentage,
                                threshold=95,
                                format_message=cpu_alert,
                                admin_ids=admin_id,
                                bot=bot))

    #Мониторинг температуры процессора
    asyncio.create_task(watcher(name='TEMP',
                                get_value=get_cpu_temp,
                                threshold=75,
                                format_message=temp_alert,
                                admin_ids=admin_id,
                                bot=bot))

    #Мониторинг количества использования оперативной пямяти
    asyncio.create_task(watcher(name='RAM',
                                get_value=get_ram_percentage,
                                threshold=80,
                                format_message=ram_alert,
                                admin_ids=admin_id,
                                bot=bot))

    #Мониторинг количества свободного места на диске
    asyncio.create_task(watcher(name='DISC',
                                get_value=get_storage_percentage,
                                threshold=80,
                                format_message=disk_alert,
                                admin_ids=admin_id,
                                bot=bot))







async def watcher(
        *,
        name: str,
        get_value: Callable,
        threshold : float,
        format_message: Callable,
        bot: Bot,
        admin_ids: List[int],
        interval: int = 60
) -> None:
    """
    :param name: имя метрики (для логов)
    :param get_value: функция, возвращающая текущее значение (float)
    :param threshold: порог
    :param format_message: функция форматирования уведомления
    :param bot:  экземпляр Bot
    :param admin_ids: кому отправлять уведомление
    :param interval: интервал с которым будет проведена проверка
    :return: None
    """


    notified = False
    logger.info(f"Запущен мониторинг {name}")

    while True:
        try:
            value = get_value()
            if value > threshold and not notified:
                notified = True
                for admin_id in admin_ids:
                    await bot.send_message(admin_id, format_message(value))
                logger.warning(format_message(value))
            if value < threshold:
                notified = False
        except Exception as e:
            logger.exception(e)

        await asyncio.sleep(interval)