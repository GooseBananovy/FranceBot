import asyncio
import os
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
from telegram import Bot
from telegram.constants import ParseMode

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
DB_PATH = 'MessageLogger/message_storage.db'

class MessageLogger:

    def __init__(self):
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                role TEXT NOT NULL,
                text TEXT NOT NULL
            )
            ''')
            conn.commit()

    def add_record(self, role: str, text: str):

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with sqlite3.connect(DB_PATH) as conn:
            conn.execute('''INSERT INTO messages (timestamp, role, text) VALUES (?, ?, ?)''',
                     (timestamp, role, text))
            conn.commit()

        asyncio.create_task(
            send_telegram_group(timestamp, role, text)
        )


async def send_telegram_group(timestamp: str, role: str, text: str) -> None:

    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print('Error: Telegram bot token or telegram chat id not set')
        return

    try:
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        formatted_message = (
            f"🕒 *{timestamp}*\n"
            f"👤 *{role.upper()}*\n"
            f"📝\n{text}"
        )

        await bot.send_message(TELEGRAM_CHAT_ID, formatted_message)

    except Exception as e:
        print(f' Telegram Logger Error: {e}')