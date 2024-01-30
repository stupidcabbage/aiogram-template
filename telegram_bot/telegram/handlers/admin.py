from aiogram import Router, types
from aiogram.filters import Command

from telegram_bot.templates import render_template
from telegram_bot.db.crud.users import get_users_count

router = Router()


@router.message(Command("admin"))
async def admin_handler(message: types.Message) -> None:
    users_count = await get_users_count()
    await message.answer(await render_template("admin.j2",
                                               {"users_count": users_count}))
