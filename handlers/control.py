import asyncio
import subprocess
from typing import Callable

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from filters import IsAdminFilter
from utils.control import kill_task, update_project

router = Router()

router.message.filter(IsAdminFilter())

@router.message(Command('reboot'))
async def reboot_handler(message: Message):
    await message.answer(" Перезагрузка системы...")
    subprocess.run(
        ["systemctl", "reboot"],
        check=True
    )

@router.message(Command('poweroff'))
async def power_off_handler(message: Message):
    await message.answer(" Выключение системы...")
    subprocess.run(
        ["systemctl", "poweroff"],
        check=True
    )

@router.message(Command("kill"))
async def kill_handler(message: Message):
    parts = message.text.split()

    if len(parts) < 2:
        await message.answer("Использование: /kill <PID> [-9]")
        return

    if not parts[1].isdigit():
        await message.answer("PID должен быть числом")
        return

    pid = int(parts[1])
    force = len(parts) == 3 and parts[2] == "-9"

    result = await asyncio.to_thread(kill_task, pid, force)
    await message.answer(result)




@router.message(Command("update"))
async def update_handler(message: Message):
    await message.answer("Начинаю обновление…")
    result = await asyncio.to_thread(update_project)
