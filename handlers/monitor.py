import asyncio

from aiogram import Router, F
from aiogram.types import Message

from utils.metrics import get_cpu_percentage, get_ram_percentage,get_cpu_temp,get_storage_percentage, get_top_processes



router = Router()


@router.message(F.text == '/status')
async def status_handler(message: Message):
    cpu = asyncio.to_thread(get_cpu_percentage)
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


@router.message(F.text == '/top')
async def top_handler(message: Message):
    msg = await asyncio.to_thread(get_top_processes)
    await message.answer(msg)
