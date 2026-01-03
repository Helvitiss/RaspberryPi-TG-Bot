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


def get_top_processes(limit: int = 5) -> List[Dict]:
    """
    Возвращает список топ-процессов по CPU (нормализован к 0–100%).
    """

    processes: List[Dict] = []

    for proc in psutil.process_iter(attrs=["pid", "name"]):
        try:
            cpu = proc.cpu_percent(None)
            memory = proc.memory_percent()

            processes.append({
                "pid": proc.info["pid"],
                "name": proc.info["name"] or "unknown",
                "cpu": round(cpu / psutil.cpu_count(), 1),
                "memory": round(memory, 1),
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes.sort(key=lambda p: p["cpu"], reverse=True)
    return processes[:limit]



if __name__ == "__main__":
    print(get_top_processes())