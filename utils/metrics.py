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




def get_top_processes() -> str:
    result = subprocess.run(
        ['top', '-b', '-n', '2'],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.splitlines()[15]


if __name__ == "__main__":
    print(get_top_processes())