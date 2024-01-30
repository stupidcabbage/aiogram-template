import asyncio
import logging
import sys
from typing import NoReturn

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from telegram_bot.config import BOT_TOKEN
from telegram_bot.telegram.handlers import admin, start

HANDLERS = (admin.router, start.router)
dp = Dispatcher()


async def main() -> NoReturn:
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    for handler in HANDLERS:
        dp.include_router(handler)
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
