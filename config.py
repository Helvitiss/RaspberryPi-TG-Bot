import os
from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
ALLOWED_USERS = '662529148'



def is_allowed_user(user):
    return str(user) in ALLOWED_USERS