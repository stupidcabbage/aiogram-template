from aiogram import Router, types
from aiogram.filters import CommandStart

from telegram_bot.db.crud.users import create_user, is_user_exists


router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message) -> None:
    if not await is_user_exists(message.from_user.id):
        await create_user(message.from_user.id)
    await message.answer("start")
