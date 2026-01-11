from dictionary import disk_alert, ram_alert, cpu_alert, temp_alert, top_msg, status_msg


def test_ram_alert():
    result = ram_alert(80)
    assert "оперативной памяти" in result
    assert result.endswith("80%")


def test_temp_alert():
    result = temp_alert(75.5)
    assert "Температура CPU" in result
    assert "75.5" in result


def test_disk_alert():
    result = disk_alert(90)
    assert "диска" in result
    assert "90%" in result


def test_cpu_alert():
    result = cpu_alert(50)
    assert "процессора" in result
    assert "50%" in result


def test_status_msg():
    result = status_msg(cpu=10, ram=20, disk=30, temps=40)

    assert "CPU: 10%" in result
    assert "RAM: 20%" in result
    assert "Disk: 30%" in result
    assert "Temp: 40" in result


def test_top_msg():
    sample_lines = [
        "1 root 20 0 25376 14848 10144 S 0.0 0.2 0:02.75 systemd",
        "2 root 20 0 0 0 0 S 1.5 0.1 0:00.01 kthreadd",
    ]

    result = top_msg(sample_lines)

    lines = result.strip().splitlines()
    assert len(lines) == 2

    assert "1" in lines[0]
    assert "0.0" in lines[0]
    assert "0.2" in lines[0]
    assert "systemd" in lines[0]

    assert "2" in lines[1]
    assert "1.5" in lines[1]
    assert "0.1" in lines[1]
    assert "kthreadd" in lines[1]
