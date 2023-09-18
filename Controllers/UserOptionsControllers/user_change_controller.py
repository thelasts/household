import asyncio
from typing import Tuple

from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from Controllers.UserOptionsControllers.help_functions import send_cancel_menu_to_callback, \
    send_submenu_to_callback, get_user_id, delete_menu_message, incorrect_user_argument, delete_message, \
    request_message, get_user_name, write_change_user_argument, get_default_payment
from Models.User import User
from Utils.FSM.UserOptions.UserOptionsFSM import UserOptionsFSM
from Utils.Keyboards.Inline.UserOptions.user_options_keyboards import get_user_change_menu


async def check_user_id_controller(message: Message, state: FSMContext) -> bool:
    back_to_menu = False
    error_message = 'Please provide the ID of the change user or their contact'

    # delete old message
    asyncio.create_task(delete_menu_message(state))

    # check message is contact or id number
    user_id, error_message = await get_user_id(error_message, message)

    #  if message is not correct return error message
    if user_id is None:
        asyncio.create_task(incorrect_user_argument(message, state, error_message))
        return back_to_menu

    user = User.get_or_none(id=user_id)
    if user is None:
        back_to_menu = True
        error_message = "This user does not exist"
        new_message = await message.answer(error_message)
        asyncio.create_task(delete_message(new_message, 10))
        await state.clear()
        return back_to_menu

    # it is all correct
    await state.update_data(user_id=user_id)
    return back_to_menu


async def open_change_user_menu_controller(request, state: FSMContext):
    message = request
    if type(request) is CallbackQuery:
        request.answer()
        message = request.message

    message_text = 'Change user menu'
    keyboard = get_user_change_menu()
    await state.set_state(UserOptionsFSM.state_open_change_menu)
    await message.answer(message_text, reply_markup=keyboard)
    asyncio.create_task(delete_message(message))


async def request_user_name_controller(call: CallbackQuery, state: FSMContext):
    new_state = UserOptionsFSM.state_change_name
    message_text = 'Please provide the new name of the user'
    await request_message(message_text, call, state, new_state)


async def request_user_default_payment_controller(call: CallbackQuery, state: FSMContext):
    new_state = UserOptionsFSM.state_change_default_payment
    message_text = 'Please provide the new default payments of the user'
    await request_message(message_text, call, state, new_state)


async def change_user_name_controller(message: Message, state: FSMContext):
    user_name, error_message = await get_user_name(message)

    asyncio.create_task(delete_menu_message(state))

    if user_name is None:
        asyncio.create_task(incorrect_user_argument(message, state, error_message))
        return

    # it is all correct
    await state.update_data(user_name=user_name)
    info_message = await message.answer(f'New name was recorded: {user_name}')
    asyncio.create_task(write_change_user_argument(message, info_message, state))


async def change_default_payment_controller(message: Message, state: FSMContext):
    user_default_payment, error_message = await get_default_payment(message)

    asyncio.create_task(delete_menu_message(state))

    if user_default_payment is None:
        asyncio.create_task(incorrect_user_argument(message, state, error_message))
        return

    # it is all correct
    await state.update_data(default_payment=user_default_payment)
    info_message = await message.answer(f'New default payment was recorded: {user_default_payment}')
    asyncio.create_task(write_change_user_argument(message, info_message, state))


async def change_user_controller(call: CallbackQuery, state: FSMContext):
    await call.answer()
    state_data = await state.get_data()
    user_id = state_data.get('user_id')
    user_name = state_data.get('user_name')
    default_payment = state_data.get('default_payment')
    info_message = ''

    user = User.get_or_none(id=user_id)

    if user is None:
        error_message = "This user does not exist"
        info_message = await call.message.answer(error_message)
        asyncio.create_task(delete_message(info_message, 10))
    else:
        if user_name:
            info_message += 'User name was change.'
            user.name = user_name

        if default_payment:
            info_message += 'Default payment was change.'
            user.default_payment = default_payment

        user.save()

        if info_message != '':
            message = await call.message.answer(info_message)
            asyncio.create_task(delete_message(message, 10))

    await state.clear()
    return call.message


async def main_cancel_controller(call: CallbackQuery, state: FSMContext) -> Message:
    await call.answer()
    await state.clear()
    message = call.message
    return message
