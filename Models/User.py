
from peewee import *

from Models import BaseModel


class User(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=250, null=False)
    default_payment = IntegerField(null=False)

    class Meta:
        table_name = 'users'
        primary_key = False
