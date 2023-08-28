from peewee import *
import os

db = SqliteDatabase(os.path.join('bot.db'))


class BaseModel(Model):
    class Meta:
        database = db
