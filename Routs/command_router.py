from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from Controllers.command_controller import start_controller, help_controller, stop_controller

command_router = Router(name="commands")


@command_router.message(CommandStart())
async def start_command(message: Message):
    await start_controller(message)


@command_router.message(Command("help"))
async def help_command(message: Message):
    await help_controller(message)


@command_router.message(Command("stop"))
async def stop_command(message: Message):
    await stop_controller(message)


@command_router.message(F.text, ValidPurchaseFilter())
async def listen_message(message: Message):
    await message.reply(add_purchase(message))


@command_router.message(Command("show_purchases"))
async def show_purchases_command(message: Message):
    await show_purchases_controller(message)
