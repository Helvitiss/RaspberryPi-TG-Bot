# RaspberryPi Telegram Bot

> Telegram-бот для удалённого управления и мониторинга Raspberry Pi. Работает в production на реальном железе как systemd-сервис.

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![aiogram](https://img.shields.io/badge/aiogram-3.x-009688?logo=telegram&logoColor=white)](https://aiogram.dev/)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

---

## О проекте

Написан под конкретную задачу: управлять Raspberry Pi удалённо без SSH и веб-интерфейса — прямо из Telegram. Бот запущен как `systemd`-сервис, работает 24/7 и отправляет алерты при перегрузке CPU, RAM, диска или перегреве.

Доступ к командам защищён белым списком `ALLOWED_USERS` — посторонний пользователь не сможет ни получить данные, ни отправить команду управления.

---

## Возможности

### Мониторинг
- Текущие метрики по команде `/status` — CPU, RAM, диск, температура
- Топ-10 ресурсоёмких процессов `/top` в табличном виде
- Фоновые watcher-задачи с настраиваемыми порогами — бот сам пришлёт уведомление, когда что-то выйдет за норму

| Метрика | Порог по умолчанию |
|---|---|
| CPU | 95% |
| RAM | 80% |
| Диск | 80% |
| Температура CPU | 75°C |

### Управление
- `/kill <pid>` — завершить процесс (SIGTERM), с флагом `-9` — принудительно (SIGKILL). Защита от завершения системных процессов (PID 0/1, kworker, kthreadd)
- `/reboot` — перезагрузка через `systemctl`
- `/poweroff` — выключение через `systemctl`
- `/update` — `git pull` + автоматический рестарт сервиса без SSH

---

## Архитектура

```
├── handlers/
│   ├── monitor.py     # /status, /top
│   └── control.py     # /kill, /reboot, /poweroff, /update
├── utils/
│   ├── metrics.py     # psutil: CPU, RAM, диск, температура
│   ├── control.py     # логика kill/update
│   └── notifications.py  # watcher-цикл и алерты
├── core/
│   ├── config.py      # настройки из .env
│   └── startup.py     # инициализация при старте
├── dictionary.py      # форматирование сообщений
├── filters.py         # IsAdminFilter — whitelist пользователей
└── tests/             # тесты форматирования сообщений
```

Мониторинг реализован через независимые async-задачи (`asyncio.create_task`) — каждая метрика проверяется отдельно с интервалом 60 секунд и не блокирует остальные.

---

## Технологический стек

| | |
|---|---|
| **Bot framework** | aiogram 3 |
| **Метрики системы** | psutil |
| **Инфраструктура** | systemd, polkit |
| **Тесты** | pytest |

---

## Быстрый старт

```bash
git clone https://github.com/Helvitiss/RaspberryPi-TG-Bot.git
cd RaspberryPi-TG-Bot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env_example .env
```

Заполни `.env`:

```env
BOT_TOKEN=your_bot_token
ALLOWED_USERS=123456789,987654321
```

Запуск:

```bash
python main.py
```

---

## Запуск как systemd-сервис

Создай файл `/etc/systemd/system/raspberry-bot.service`:

```ini
[Unit]
Description=Raspberry Pi Telegram Bot
After=network.target

[Service]
User=user
WorkingDirectory=/home/user/RaspberryPi-TG-Bot
EnvironmentFile=/home/user/RaspberryPi-TG-Bot/.env
ExecStart=/home/user/RaspberryPi-TG-Bot/.venv/bin/python main.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable raspberry-bot
sudo systemctl start raspberry-bot
```

---

## Настройка polkit

Чтобы бот мог выполнять `reboot` и `poweroff` без sudo, добавь правило polkit в `/etc/polkit-1/rules.d/99-raspberry-bot.rules`:

```js
polkit.addRule(function(action, subject) {
    if (
        subject.user === "user" &&
        (
            action.id === "org.freedesktop.login1.reboot" ||
            action.id === "org.freedesktop.login1.power-off" ||
            action.id === "org.freedesktop.systemd1.manage-units"
        )
    ) {
        return polkit.Result.YES;
    }
});
```

---

## Тесты

```bash
pytest tests/ -v
```

Покрыта логика форматирования всех системных сообщений — алерты, статус, топ процессов.

---

## Лицензия

[MIT](LICENSE)
