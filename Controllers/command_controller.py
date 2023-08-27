from aiogram.types import Message
from Controllers.const import FORMAT, COMMANDS

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
