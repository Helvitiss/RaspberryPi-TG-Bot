import psutil
import logging

logger = logging.getLogger(__name__)


def warmup_psutil_cpu() -> None:
    """
    Прогревает CPU-счётчики psutil.

    Нужно для корректной работы cpu_percent()
    без блокирующих interval > 0.
    """

    logger.info("Разогреваю psutil")

    for proc in psutil.process_iter():
        try:
            proc.cpu_percent(None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Также прогреваем общий CPU
    psutil.cpu_percent(None)

    logger.info("Разогрев успешный ")