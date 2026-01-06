import asyncio

from aiogram import Router, F
from aiogram.types import Message

from utils.metrics import get_cpu_percentage, get_ram_percentage,get_cpu_temp,get_storage_percentage, get_top_processes
from dictionary import status_msg, top_msg

router = Router()


@router.message(F.text == '/status')
async def status_handler(message: Message):
    cpu = await asyncio.to_thread(get_cpu_percentage)
    ram = get_ram_percentage()
    disk = get_storage_percentage()
    temps = get_cpu_temp()

    reply = status_msg(cpu=cpu, ram=ram, disk=disk, temps=temps)

    await message.answer(reply)


@router.message(F.text == '/top')
async def top_handler(message: Message):
    top_lines_list = await asyncio.to_thread(get_top_processes)
    msg = top_msg(top_lines_list)
    await message.answer(str(msg))
