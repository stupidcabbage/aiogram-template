from aiogram import Router, types
from aiogram.filters import CommandStart

from src.db.crud.users import create_user, is_user_exists
from src.templates import render_template

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message) -> None:
    if not await is_user_exists(message.from_user.id):
        await create_user(message.from_user.id)
    await message.answer(await render_template("start.j2"))
