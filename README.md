
# Python Aiogram template

Start template for for telegram bots on python + aiogram.



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`BOT_TOKEN` - Telegram token for your bot. You can get it from [BotFather](https://t.me/BotFather)



## Deployment

To deploy this project run

Install poetry as python dependency management

```bash
  pip3 install poetry
```
Install dependencies
```bash
  poetry install
```
Run ENV
```bash
  poetry shell
```
Make migrations
```bash
  alembic upgrade head
```
Start BOT
```bash
  poetry run python3 -m src
```


## Features

- Admin panel with users count (You have to change your admin status to TRUE in the DB)
- Text templates (with Jinja2)
