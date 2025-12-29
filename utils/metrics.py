from psutil import virtual_memory, sensors_temperatures, disk_usage


def get_ram_percentage() -> float:
    result = virtual_memory().percent
    return result


def get_cpu_temp() -> float:
    temp = sensors_temperatures().get('cpu_thermal')[0].current
    return temp


def get_storage_percentage() -> float:
    result = disk_usage('/').percent
    return result

