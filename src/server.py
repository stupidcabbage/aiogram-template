import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqladmin import Admin

from src.api.admin import add_views
from src.config import TEMPLATES_DIR
from src.db.crud.session import engine

from src.api.root import root_router


@asynccontextmanager
async def lifespan(application: FastAPI):
    logging.info("🚀 Starting application")
    from src.bot import start_telegram
    await start_telegram()
    yield
    logging.info("⛔ Stopping application")


app = FastAPI(lifespan=lifespan)
app.include_router(root_router)

admin = Admin(app, engine=engine,
              templates_dir=TEMPLATES_DIR)
add_views(admin)
