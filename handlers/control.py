import subprocess
from typing import Callable

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from filters import IsAdminFilter

router = Router()

router.message.filter(IsAdminFilter())

@router.message(F.text == "/reboot")
async def reboot_handler(message: Message):


    await message.answer("💻 Перезагрузка системы...")
    subprocess.run(["sudo","reboot"], shell=True)


@router.message(F.text == "/poweroff")
async def power_off_handler(message: Message):
    await message.answer("💻 Выключение системы...")
    subprocess.run(['sudo', 'poweroff'], shell=True)


@router.message(Command("kill"))
async def kill_handler(message: Message):
    parts = message.text.split()

    await message.answer(str(parts))