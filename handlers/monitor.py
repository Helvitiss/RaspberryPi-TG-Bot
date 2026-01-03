import subprocess

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from utils.metrics import get_cpu_percentage, get_ram_percentage,get_cpu_temp,get_storage_percentage




router = Router()


@router.message(F.text == '/status')
async def status_handler(message: Message):

    cpu = get_cpu_percentage()
    ram = get_ram_percentage()
    disk = get_storage_percentage()
    temps = get_cpu_temp()

    reply = (
        f"💻 Статус системы:\n"
        f"CPU: {cpu}%\n"
        f"RAM: {ram}%\n"
        f"Disk: {disk}%\n"
        f"Temp: {temps}"
    )
    await message.answer(reply)


