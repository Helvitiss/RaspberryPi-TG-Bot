from aiogram.filters import BaseFilter
from aiogram.types import Message

from core.config import ALLOWED_USERS


class IsAdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in ALLOWED_USERS
