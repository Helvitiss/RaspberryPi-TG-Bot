import psutil, logging

def warming_up():
    try:
        psutil.cpu_percent(None)
    except Exception as e:
        logging.getLogger(__name__).exception(e)