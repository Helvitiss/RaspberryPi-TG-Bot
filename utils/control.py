import subprocess

import psutil



FORBIDDEN_PIDS = {0, 1}


def kill_task(pid: int, force: bool = False) -> str:
    """
    Завершает процесс по PID.

    force=False -> SIGTERM (мягко)
    force=True  -> SIGKILL (жёстко)
    """

    if pid in FORBIDDEN_PIDS:
        return " Этот процесс запрещено завершать"

    try:
        proc = psutil.Process(pid)

        # Защита от kernel threads
        if proc.name().startswith("kworker") or proc.name().startswith("kthreadd"):
            return " Kernel-процессы завершать нельзя"

        proc.terminate()

        try:
            proc.wait(timeout=3)
            return f" Процесс {pid} завершён (SIGTERM)"

        except psutil.TimeoutExpired:
            if not force:
                return f"⚠ Процесс {pid} не завершился за 3 сек"

            proc.kill()
            proc.wait(timeout=2)
            return f" Процесс {pid} убит принудительно (SIGKILL)"

    except psutil.NoSuchProcess:
        return f" Процесс {pid} не найден"

    except psutil.AccessDenied:
        return f" Нет прав для завершения процесса {pid}"

    except Exception as e:
        return f" Ошибка: {e}"


def update_project() -> str:
    """
    Пулит код из гита и перезапускает бота
    """
    try:
        pull = subprocess.run(
            ["git", "pull"],
            capture_output=True,
            text=True,
            check=True
        )

        subprocess.run(
            ["systemctl", "restart", "raspberry-bot"],
            check=True
        )

        return f"Обновление выполнено:\n{pull.stdout}"

    except subprocess.CalledProcessError as e:
        return f"Ошибка обновления:\n{e.stderr}"