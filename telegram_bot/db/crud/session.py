from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from telegram_bot.config import PATH_TO_DB


engine = create_async_engine(f"sqlite+aiosqlite:///{PATH_TO_DB}", echo=True)
Session = async_sessionmaker(engine, expire_on_commit=False)
