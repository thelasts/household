import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO)

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
COMMANDS = os.getenv("COMMANDS")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_polling(message: types.Message):
    await message.answer("household start message")

@dp.message_handler(commands=['help'])
async def show_help(message: types.Message):
    await message.answer(f"the list of available commands:\n"
                         f"<pre>{COMMANDS}</pre>", parse_mode='html')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
