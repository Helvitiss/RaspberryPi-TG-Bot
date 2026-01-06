import subprocess

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


def get_top_processes(limit: int = 10) -> str:
    result = subprocess.run(
        ['top', '-b', '-n', '2'],
        capture_output=True,
        text=True,
        check=True
    )

    lines = result.stdout.splitlines()

    header_index = None
    #находим индекс хедера у top
    for i, line in enumerate(lines):
        if line.strip().startswith("PID USER"):
            header_index = i
            break

    if header_index is None:
        return "Не удалось найти таблицу процессов"

    process_lines = lines[header_index: header_index + 1 + limit]

    # return "\n".join(process_lines)
    return process_lines

if __name__ == "__main__":
    print(get_top_processes())
