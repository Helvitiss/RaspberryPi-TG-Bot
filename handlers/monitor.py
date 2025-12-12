import subprocess

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
import psutil

from config import is_allowed_user

router = Router()


@router.message(F.text == '/status')
async def status_handler(message: Message):
    if not is_allowed_user(message.from_user.id):
        return message.answer('У вас нет доступа')


    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    temps = psutil.sensors_temperatures()
    temp_str = ""
    if "cpu-thermal" in temps:
        temp_str = f"{temps['cpu-thermal'][0].current:.1f}°C"
    elif temps:
        # берем первую доступную
        first_sensor = list(temps.values())[0][0]
        temp_str = f"{first_sensor.current:.1f}°C"
    else:
        temp_str = "N/A"
    reply = (
        f"💻 Статус системы:\n"
        f"CPU: {cpu}%\n"
        f"RAM: {ram}%\n"
        f"Disk: {disk}%\n"
        f"Temp: {temp_str}"
    )
    await message.answer(reply)


