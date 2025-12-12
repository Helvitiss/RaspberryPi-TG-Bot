import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="[{asctime}] [{levelname}] {message}",
        style="{",
    )