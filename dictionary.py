


def temp_alert(value: float) -> str:
    return f"🔥 ВНИМАНИЕ\nТемпература CPU: {value}"


def ram_alert(value: float) -> str:
    return f'ВНИМАНИЕ\nИспользование оперативной памяти: {value}%'

def disk_alert(value: float) -> str:
    return f'ВНИМАНИЕ\nИспользование диска: {value}%'

def cpu_alert(value: float) -> str:
    return f'ВНИМАНИЕ\nИспользование процессора: {value}%'