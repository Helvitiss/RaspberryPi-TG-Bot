import logging


# Настроим логирование
def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)


    return logger

# Логирование старта
def log_start():
    logger = setup_logging()
    logger.info("Бот был перезапущен!")
