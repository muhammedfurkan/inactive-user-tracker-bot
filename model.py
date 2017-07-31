from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase('messages.db')


class BaseModel(Model):
    class Meta:
        database = db


class Message(BaseModel):
    chat_id = IntegerField()
    from_id = IntegerField()
    last_commit = DateTimeField()
    commit_count = IntegerField()
