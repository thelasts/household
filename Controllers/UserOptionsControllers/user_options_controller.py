import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from Controllers.UserOptionsControllers.help_functions import delete_message, send_submenu_to_callback
from Utils.FSM.UserOptions.UserOptionsFSM import UserOptionsFSM
from Utils.Keyboards.Inline.UserOptions.user_options_keyboards import get_user_options_menu, get_user_add_menu, \
    get_user_change_menu


async def open_user_option_menu_controller(message: Message, state: FSMContext):
    message_text = 'User options'
    await state.set_state(UserOptionsFSM.state_user_options_menu_open)
    await message.answer(message_text, reply_markup=get_user_options_menu())
    asyncio.create_task(delete_message(message))


async def close_user_option_menu_controller(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.answer()
    asyncio.create_task(delete_message(call.message))


async def open_user_add_menu_controller(call: CallbackQuery, state: FSMContext):
    message_text = 'Add user menu'
    keyboard = get_user_add_menu()
    await state.set_state(UserOptionsFSM.state_open_add_user_menu)
    await send_submenu_to_callback(message_text, keyboard, state, call)
