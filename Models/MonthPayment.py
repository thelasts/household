from peewee import *

from Models import BaseModel
from Models import User


class MonthPayment(BaseModel):
    buy_name = TextField(null=False)
    owner_id = ForeignKeyField(User, backref="month_payments")
    buy_price = IntegerField(null=False)
    buy_date = DateField(null=False)

    class Meta:
        table_name = 'month_payments'
