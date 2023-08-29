from aiogram.types import Message
from Controllers.const import *
from Models import db, MonthPayment

STOP = False


async def start_controller(message: Message):
    global STOP
    STOP = False
    await message.reply(f"Hi! {FORMAT}")


async def help_controller(message: Message):
    await message.answer(f"The list of available commands:\n"
                         f"<pre>{COMMANDS}</pre>\n\n{FORMAT}")


async def stop_controller(message: Message):
    global STOP
    STOP = True
    await message.answer("Polling stopped. No new purchases will be saved")


async def show_purchases_controller(message: Message):
    with db:
        result = TABLESEP
        purchases = MonthPayment.select()
        for p in purchases:
            result += f'<i>{p.buy_name}-{p.buy_price}</i>\n'
        result += TABLESEP
    await message.answer(f"Here's what I've found:\n{result}More data soon")
