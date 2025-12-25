import logging
from aiogram import Bot
from config import BOT_TOKEN, ALLOWED_USER

bot = Bot(token=BOT_TOKEN)

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger

