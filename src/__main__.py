import asyncio
import logging
import sys
from typing import NoReturn

from aiogram import Dispatcher

from src.config import bot
from src.telegram.handlers import admin, start

HANDLERS = (admin.router, start.router)
dp = Dispatcher()


async def main() -> NoReturn:
    await bot.delete_webhook()
    for handler in HANDLERS:
        dp.include_router(handler)
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
