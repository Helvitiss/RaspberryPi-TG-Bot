import asyncio

from aiogram import Bot

from core.config import ALLOWED_USERS
from core.logging_conf import setup_logging, log_start
from utils.notifications import setup_all_watchers, startup_notification
from core.warming import warmup_psutil_cpu




async def startup(bot: Bot):
    """
    Автозапуск самого главного
    """

    setup_logging()
    log_start()

    warmup_psutil_cpu()

    asyncio.create_task(
        setup_all_watchers(bot, ALLOWED_USERS)
    )

    await startup_notification(bot, ALLOWED_USERS)
