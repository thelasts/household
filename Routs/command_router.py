from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from Controllers import start_controller, help_controller, stop_controller

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
