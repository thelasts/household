from aiogram import Bot
from aiogram.types import Message
from Controllers.const import *
from Models import db, MonthPayment

STOP = False


async def start_controller(message: Message):
    global STOP
    STOP = False
    await message.reply(f"Hi! {FORMAT}")


async def help_controller(message: Message, bot: Bot):
    commands = await bot.get_my_commands()
    for c in commands:
        print(c.command)
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
            result += f'<i>{p.id}-{p.buy_name}-{p.buy_price}</i>\n'
        result += TABLESEP
    await message.answer(f"Here's what I've found:\n{result}More data soon")
