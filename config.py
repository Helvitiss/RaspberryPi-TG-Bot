import os
from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
ALLOWED_USER = 662529148



def is_allowed_user(user):
    return int(user) == ALLOWED_USER