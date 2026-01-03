import time
from typing import Dict, List

import psutil


def get_ram_percentage() -> float:
    result = psutil.virtual_memory().percent
    return result


def get_cpu_temp() -> float:
    temp = psutil.sensors_temperatures().get('cpu_thermal')[0].current
    return temp


def get_storage_percentage() -> float:
    result = psutil.disk_usage('/').percent
    return result

def get_cpu_percentage() -> float:
    result = psutil.cpu_percent(interval=1)
    return result


import subprocess


def get_top_processes(limit: int = 5) -> str:
    cmd = [
        "ps",
        "-eo", "pid,comm,%cpu,%mem",
        "--sort=-%cpu"
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=True
    )

    lines = result.stdout.strip().splitlines()
    header = lines[0]
    body = lines[1:limit + 1]

    return "\n".join([header] + body)




if __name__ == "__main__":
    print(get_top_processes())