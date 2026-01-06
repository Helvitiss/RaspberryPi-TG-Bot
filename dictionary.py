


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
        i = i.split()
        reply += f'{i[pid]: ^6} {i[cpu]: ^6} {i[mem]: ^6} {i[command]: ^7}\n'

    return reply


if __name__ == "__main__":
    a = ['    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND', '      342 root      20   0   25376  14848  10144 S   100.0   100.2   0:02.75 systemd', '      2 root      20   0       0      0      0 S   0.0   0.0   0:00.00 kthreadd', '      3 root      20   0       0      0      0 S   0.0   0.0   0:00.00 pool_wo+', '      4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker+', '      5 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker+', '      6 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker+', '      7 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker+', '      8 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker+', '     12 root      20   0       0      0      0 I   0.0   0.0   0:00.00 kworker+', '     13 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker+']
    print(top_msg(a))