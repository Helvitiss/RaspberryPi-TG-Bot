import logging
from aiogram import Bot


logger = logging.getLogger(__name__)

async def startup_notification(bot: Bot, admin_id: int):
    """Отправляет по определенному айди сообщение о запуске системы"""

    try:
        await bot.send_message(admin_id, 'Система запущена')
        logger.info('Уведомление о запуске системы отправленно ')
    except Exception as e:
        logger.error(e)