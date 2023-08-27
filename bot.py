import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO)

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN, parse_mode="html")
dp = Dispatcher(bot)

COMMANDS = ['start', 'help']
FORMAT = 'To add a valid purchase statement please follow the given format:\n\n"<i>! item name, price</i>"'
LANG = "en" #TODO
STOP = False

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global STOP
    STOP = False
    await message.reply(f"Hi! {FORMAT}")


@dp.message_handler(commands=['help'])
async def show_help(message: types.Message):
    await message.answer(f"The list of available commands:\n"
                         f"<pre>{COMMANDS}</pre>\n\n{FORMAT}")

@dp.message_handler(commands=['stop'])
async def stop_polling(message: types.Message):
    global STOP
    STOP = True
    await message.answer("Polling stopped. No new purchases will be saved")


#TODO parser
@dp.message_handler()
async def catch_purchase(message: types.Message):
    if not STOP and message.text[0] == "!":
        username = message.from_user.first_name
        purchase = message.text.split('!')[-1].strip()
        await message.reply(f"New purchase by <i>{username}</i> "
                            f"is added: <i>{purchase}</i>")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
