import subprocess

from aiogram import Router, F
from aiogram.types import Message

from config import is_allowed_user

router = Router()


@router.message(F.text == "/reboot")
async def reboot_handler(message: Message):
    if not is_allowed_user(message.from_user.id):
        return await message.answer("❌ У вас нет прав.")

    await message.answer("💻 Перезагрузка системы...")
    subprocess.run("sudo reboot", shell=True)


@router.message(F.text == "/poweroff")
async def poweroff_handler(message: Message):
    if not is_allowed_user(message.from_user.id):
        return await message.answer("❌ У вас нет прав.")

    await message.answer("💻 Выключение системы...")
    subprocess.run("sudo poweroff", shell=True)
