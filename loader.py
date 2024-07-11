from config_data.config import BOT_TOKEN, DB_NAME
from database.db import initialize_db


def load_config():
    return {
        "bot_token": BOT_TOKEN,
        "db_name": DB_NAME
    }


def initialize():
    initialize_db()
