import logging

from aiogram import Bot, Dispatcher, types

from src.config import TELEGRAM_SECRET_TOKEN, TELEGRAM_WEBHOOK_URL, bot
from src.telegram.handlers import admin, start

HANDLERS = (admin.router, start.router)
dp = Dispatcher()


async def start_telegram() -> None:
    await bot.delete_webhook()
    for handler in HANDLERS:
        dp.include_router(handler)

    await start_webhook(bot)


async def start_webhook(my_bot: Bot) -> None:
    async def check_webhook() -> types.WebhookInfo | None:
        try:
            webhook_info = await my_bot.get_webhook_info()
            return webhook_info
        except Exception as e:
            logging.error(f"Can't get webhook info - {e}")
            return
    current_webhook_info = await check_webhook()
    logging.info("Current webhook info:", current_webhook_info)
    try:
        await bot.set_webhook(
                TELEGRAM_WEBHOOK_URL,
                drop_pending_updates=current_webhook_info.pending_update_count > 0,
                secret_token=TELEGRAM_SECRET_TOKEN,
                max_connections=40)
        logging.info(f"Updated bot info: {await check_webhook()}")
    except Exception as e:
        logging.info(f"Can't update webhook - {e}")
