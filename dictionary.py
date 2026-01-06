


def temp_alert(value: float) -> str:
    return f"🔥 ВНИМАНИЕ\nТемпература CPU: {value}"


def ram_alert(value: float) -> str:
    return f'ВНИМАНИЕ\nИспользование оперативной памяти: {value}%'

def disk_alert(value: float) -> str:
    return f'ВНИМАНИЕ\nИспользование диска: {value}%'

def cpu_alert(value: float) -> str:
    return f'ВНИМАНИЕ\nИспользование процессора: {value}%'

def status_msg(cpu: float, ram: float, disk: float, temps:float)-> str:
    reply = (
        f"💻 Статус системы:\n"
        f"CPU: {cpu}%\n"
        f"RAM: {ram}%\n"
        f"Disk: {disk}%\n"
        f"Temp: {temps}"
    )
    return reply

def top_msg(process_lines: list) -> str:
    reply = f""
    pid = 0
    cpu = 8
    mem = 9
    command = 11
    for i in process_lines:
        reply += f'{i[pid]}, {i[cpu]}, {i[mem]}, {i[command]}\n\n'

    return reply