# RaspberryPi‑TG‑Bot

Telegram‑бот для удалённого управления и мониторинга Raspberry Pi / Linux‑сервера через Telegram.

Проект позволяет следить за состоянием системы, получать уведомления о перегрузке CPU/RAM/диска/температуры, просматривать список процессов, управлять системой (перезагрузка, выключение) и обновлять код через команду бота.

---

## 🧠 Основные возможности

✔ Мониторинг системы: CPU, RAM, диск, температура  
✔ Просмотр топ‑процессов (`/top`)  
✔ Уведомления при превышении порогов  
✔ Управление системой: перезагрузка и выключение  
✔ Автообновление через команду `/update`  
✔ Работает как сервис `systemd`  
✔ Безопасные привилегии через `polkit`  
✔ Покрыт базовыми тестами логики

---

## 🚀 Быстрый старт

### 1. Клонирование

```bash
git clone https://github.com/Helvitiss/RaspberryPi-TG-Bot.git
cd RaspberryPi-TG-Bot
```

---

### 2. Настройка виртуального окружения

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

### 3. Создание `.env`

```bash
cp .env_example .env
```

```env
BOT_TOKEN=your_bot_token_here
ADMIN_IDS=123456789,987654321
```

---

## 🧩 Запуск локально

```bash
python main.py
```

---

## ⚙️ systemd service

```ini
[Unit]
Description=Raspberry Pi Telegram Bot
After=network.target

[Service]
User=user
WorkingDirectory=/home/user/RaspberryPi-TG-Bot
EnvironmentFile=/home/user/RaspberryPi-TG-Bot/.env
ExecStart=/home/user/RaspberryPi-TG-Bot/.venv/bin/python /home/user/RaspberryPi-TG-Bot/main.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

---

## 🔐 polkit

```js
polkit.addRule(function(action, subject) {
    if (
        subject.user === "user" &&
        (
            action.id === "org.freedesktop.login1.reboot" ||
            action.id === "org.freedesktop.login1.power-off"
        )
    ) {
        return polkit.Result.YES;
    }
});


polkit.addRule(function(action, subject) {
    if (
        subject.user === "user" &&
        (
            action.id === "org.freedesktop.systemd1.manage-units"
        )
    ) {
        return polkit.Result.YES;
    }
});
```

---

## 📋 Команды

/status  
/top  
/kill <pid>  
/reboot  
/poweroff  
/update  

---




MIT License
