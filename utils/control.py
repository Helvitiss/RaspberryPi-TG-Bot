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

        # Защита от kernel threads (Linux)
        if proc.name().startswith("kworker") or proc.name().startswith("kthreadd"):
            return " Kernel-процессы завершать нельзя"

        # Мягкое завершение
        proc.terminate()

        try:
            proc.wait(timeout=3)
            return f" Процесс {pid} завершён (SIGTERM)"

        except psutil.TimeoutExpired:
            if not force:
                return f"⚠ Процесс {pid} не завершился за 3 сек"

            # Жёсткое завершение
            proc.kill()
            proc.wait(timeout=2)
            return f" Процесс {pid} убит принудительно (SIGKILL)"

    except psutil.NoSuchProcess:
        return f" Процесс {pid} не найден"

    except psutil.AccessDenied:
        return f" Нет прав для завершения процесса {pid}"

    except Exception as e:
        return f" Ошибка: {e}"