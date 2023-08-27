import asyncio
import logging
from aiogram import Bot

from Config import API_TOKEN
from dispatcher import return_dispatcher
from Models import db, User, Debit, MonthPayment

logging.basicConfig(level=logging.INFO)


def configurate_database():
    db.connect()
    db.create_tables([User, User, Debit, MonthPayment])


async def bot_start():
    bot = Bot(API_TOKEN, parse_mode="html")
    dp = return_dispatcher()
    try:
        configurate_database()
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(bot_start())
