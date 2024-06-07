from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.config import PATH_TO_DB

engine = create_async_engine(f"sqlite+aiosqlite:///{PATH_TO_DB}")
Session = async_sessionmaker(engine, expire_on_commit=False)
