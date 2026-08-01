# 🖨️ PrintoBot

A Telegram bot that allows users to remotely send text for printing.

Instead of sending messages through messengers or social networks, users simply write to the bot, and the text is instantly printed on a connected printer.

This project was created to simplify communication between family members and automate everyday printing tasks.

---

## ✨ Features

- 📩 Receive text messages from Telegram users
- 🖨️ Automatic printing on a Canon printer
- 👤 Automatic user registration
- 📋 User list for the administrator
- 📅 Registration date tracking
- 📨 Message forwarding to the owner
- ⚙️ Environment variable configuration
- 💾 JSON-based user storage

---

## Logo

![Logo](assets/logo.png)

---

## Telegram Bot

![Bot](assets/telegram.png)

---

## Bot Work

![Work](assets/work.png)

---

## 🛠 Tech Stack

- Python 3.14
- aiogram 3
- pywin32
- python-dotenv

---

## 📂 Project Structure

```
printpbpy/
│
├── services/
│   ├── formatter.py
│   ├── printer.py
│
├── settings/
│   ├── config.py
│   ├── paths.py
│   ├── users_storage.py
│
├── storage/
│   └── users.json
│
├── handlers.py
├── bot.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/itheinkarchitect/PrintoBot.git
cd printobot
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

Create a `.env` file in the project root.

Example:

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
OWNER_ID=YOUR_TELEGRAM_ID
```

---

## ▶️ Run

```bash
python bot.py
```

---

## 🖨 Supported Printer

The project was developed and tested with

- Canon LBP2900

Printing is implemented using the Windows API (`pywin32`).

---

## 📸 Example Workflow

```
User
   │
   ▼
Telegram Bot
   │
   ▼
Bot receives message
   │
   ▼
Owner receives notification
   │
   ▼
Printer prints the text
```

---

## 📌 Future Improvements

- Print images
- PDF printing
- Queue management
- Printing history
- Web admin panel
- Multiple printer support

---

## 📄 License

This project is released under the MIT License.