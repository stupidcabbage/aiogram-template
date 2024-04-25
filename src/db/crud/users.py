import logging
from typing import Optional

from sqlalchemy import func, select

from .session import Session
from src.db.models import User


async def get_users_count() -> int:
    async with Session.begin() as session:
        stmt = select(func.count(User.telegram_id))
        users = await session.scalar(stmt)
        if not users:
            return 0
        return users


async def create_user(telegram_id: int) -> None:
    async with Session.begin() as session:
        model = User(telegram_id=telegram_id)
        session.add(model)
        logging.info(f"Created new user: {model}")


async def get_user(telegram_id: int) -> Optional[User]:
    async with Session.begin() as session:
        stmt = (
            select(User).
            where(User.telegram_id == telegram_id)
        )
        user = await session.scalar(stmt)
        return user

async def is_user_exists(telegram_id: int) -> bool:
    async with Session.begin() as session:
        stmt = (
            select(func.count(User.telegram_id)).
            where(User.telegram_id == telegram_id)
        )
        user = await session.scalar(stmt)
        return bool(user)
