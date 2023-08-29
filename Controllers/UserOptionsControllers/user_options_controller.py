import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from Controllers.UserOptionsControllers.help_functions import delete_message
from Utils.FSM.UserOptions import UserOptionsFSM
from Utils.Keyboards.Inline.UserOptions import (get_user_options_menu, get_user_add_menu)


async def open_user_option_menu_controller(message: Message, state: FSMContext):
    message_text = 'User options'
    await state.set_state(UserOptionsFSM.state_user_options_menu_open)
    asyncio.create_task(delete_message(message))
    await message.answer(message_text, reply_markup=get_user_options_menu())


async def close_user_option_menu_controller(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.answer()
    await call.message.delete()


async def open_user_add_menu_controller(call: CallbackQuery, state: FSMContext):
    message_text = 'Add user menu'
    await state.set_state(UserOptionsFSM.state_open_add_user_menu)
    await call.answer()
    await call.message.delete()
    await call.message.answer(message_text, reply_markup=get_user_add_menu())
