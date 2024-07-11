from peewee import Model, IntegerField, CharField, DateTimeField, SQL, SqliteDatabase

db = SqliteDatabase('crypto_bot.db')


class UserRequest(Model):
    user_id = IntegerField()
    command = CharField()
    timestamp = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

    class Meta:
        database = db


def initialize_db():
    db.connect()
    db.create_tables([UserRequest], safe=True)


def log_user_request(user_id: int, command: str):
    UserRequest.create(user_id=user_id, command=command)


def get_user_requests(limit=10):
    return UserRequest.select().order_by(UserRequest.timestamp.desc()).limit(limit)
