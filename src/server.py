from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging

from src.db.models import User
from sqladmin import Admin, ModelView
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

admin = Admin(app, engine=engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.telegram_id, User.created_at]


admin.add_view(UserAdmin)
