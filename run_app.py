import asyncio
import logging
from aiogram import Bot

from Config.config import API_TOKEN
from Models.BaseModel import db
from Models.Debit import Debit
from Models.MonthPayment import MonthPayment
from Models.User import User
from dispatcher import return_dispatcher


logging.basicConfig(level=logging.INFO)


def configurate_database():
    db.connect()
    db.create_tables([User, Debit, MonthPayment])


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
