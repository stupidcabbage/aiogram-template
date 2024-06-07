from sqladmin import Admin, ModelView

from src.db.models import User


class UserAdmin(ModelView, model=User):
    column_list = [User.telegram_id, User.created_at, User.is_admin]
    form_columns = [User.telegram_id, User.is_admin]
    form_args = dict(telegram_id=dict(label="Telegram ID",
                                      description="Уникальный айди пользователя."),
                     is_admin=dict(label="Администратор"))
    form_include_pk = True

    icon = "fa-solid fa-user"
    category = "Пользователи"
    name = "Пользователь"
    name_plural = "Пользователи"


VIEWS = (UserAdmin, )


def add_views(admin: Admin):
    for i in VIEWS:
        admin.add_view(i)
