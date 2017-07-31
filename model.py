from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase('messages.db')


class BaseModel(Model):
    class Meta:
        database = db


class Message(BaseModel):
    from_id = IntegerField()
    chat_id = IntegerField()
    last_commit = DateTimeField()
