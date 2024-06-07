from aiogram import Router, types
from aiogram.filters import Command

from src.db.crud.users import get_user, get_users_count
from src.templates import render_template

router = Router()


@router.message(Command("admin"))
async def admin_handler(message: types.Message) -> None:
    user = await get_user(message.from_user.id)
    if user and user.is_admin:
        users_count = await get_users_count()
        await message.answer(
                await render_template("admin.j2",
                                      {"users_count": users_count}))
