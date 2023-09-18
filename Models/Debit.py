from peewee import *

from Models.BaseModel import BaseModel
from Models.User import User


class Debit(BaseModel):
    date = DateField(null=False)
    # who pay
    payer = ForeignKeyField(User, backref="debits")
    # who is paid
    recipient = ForeignKeyField(User, backref="debits")
    amount_money = IntegerField(null=False)
    paid = BooleanField(null=False, default=0)

    class Meta:
        table_name = 'debits'
