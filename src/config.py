import os
from pathlib import Path
from typing import Any

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
PATH_TO_DB = f"{BASE_DIR.parent}/db.sqlite3"


class Env:
    def __init__(self):
        from dotenv import load_dotenv
        load_dotenv()

    def get(self, key: str, default: Any = None) -> str:
        token = os.getenv(key, default)
        if not token:
            raise self.ObligatoryValueFromEnvDoesNotExists
        return token

    def get_without_checking(self, key, default) -> str:
        return os.getenv(key, default)

    class ObligatoryValueFromEnvDoesNotExists(Exception):
        def __str__(self):
            return "Obligatory token does not exists! Check env file."


env = Env()

BOT_TOKEN = env.get("BOT_TOKEN")

SERVER_DOMEN = env.get("SERVER_DOMEN")
TELEGRAM_WEBHOOK_URL = f"https://{SERVER_DOMEN}/webhook"
TELEGRAM_SECRET_TOKEN = env.get("TELEGRAM_SECRET_TOKEN")

bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
