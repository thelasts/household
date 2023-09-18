from aiogram.types import Message

from Models import db, MonthPayment


def add_purchase(message: Message) -> str:
    cnt = message.text.split(',', 1)
    try:
        with db:
            purchase = MonthPayment.create(buy_name=cnt[0].replace("!", "").strip(),
                                                  owner_id=message.from_user.first_name,
                                                  buy_price=cnt[1].strip(),
                                                  buy_date=message.date)
    finally:
        return f'Success, {message.from_user.first_name}!'
    return 'Failed to create a model'


def show_table() -> None:
    with db:
        purchases = MonthPayment.select()
    return purchases
