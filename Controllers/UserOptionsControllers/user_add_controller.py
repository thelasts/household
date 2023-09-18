import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from Controllers.UserOptionsControllers.help_functions import delete_message, send_submenu_to_callback, \
    delete_menu_message, incorrect_user_argument, write_new_user_argument, \
    send_cancel_menu_to_callback, get_user_id, request_message
from Models.User import User
from Utils.FSM.UserOptions.UserOptionsFSM import UserOptionsFSM
from Utils.Keyboards.Inline.UserOptions.user_options_keyboards import get_user_options_menu, get_user_add_menu


async def main_cancel_controller(call: CallbackQuery, state: FSMContext) -> Message:
    await call.answer()
    await state.clear()
    message = call.message
    return message


async def request_user_id_controller(call: CallbackQuery, state: FSMContext):
    new_state = UserOptionsFSM.state_add_new_user_id
    message_text = 'Please provide the ID of the new user or their contact'
    await request_message(message_text, call, state, new_state)


async def request_user_name_controller(call: CallbackQuery, state: FSMContext):
    new_state = UserOptionsFSM.state_add_new_user_name
    message_text = 'Please provide the name of the new user'
    await request_message(message_text, call, state, new_state)


async def request_default_payment_controller(call: CallbackQuery, state: FSMContext):
    new_state = UserOptionsFSM.state_add_new_user_default_payment
    message_text = 'Please provide the default payments of the new user'
    await request_message(message_text, call, state, new_state)


async def add_user_id_controller(message: Message, state: FSMContext):
    error_message = 'Please provide the ID of the new user or their contact'

    # delete old message
    asyncio.create_task(delete_menu_message(state))

    # check message is contact or id number
    user_id, error_message = await get_user_id(error_message, message)

    #  if message is not correct return error message
    if user_id is None:
        asyncio.create_task(incorrect_user_argument(message, state, error_message))
        return

    # it is all correct
    await state.update_data(user_id=user_id)
    add_menu_message = await message.answer(f'ID was recorded: {user_id}')
    asyncio.create_task(write_new_user_argument(message, add_menu_message, state))


async def add_user_name_controller(message: Message, state: FSMContext):
    user_name = message.text
    error_message = 'Invalid name format.Write username'

    asyncio.create_task(delete_menu_message(state))

    if user_name is None:
        asyncio.create_task(incorrect_user_argument(message, state, error_message))
        return

    # it is all correct
    await state.update_data(user_name=user_name)
    add_menu_message = await message.answer(f'Name was recorded: {user_name}')
    asyncio.create_task(write_new_user_argument(message, add_menu_message, state))


async def add_user_default_payment_controller(message: Message, state: FSMContext):
    user_default_payment = None
    error_message = 'Invalid default payment format. Write number'

    asyncio.create_task(delete_menu_message(state))

    try:
        user_default_payment = int(message.text)
    except (ValueError, TypeError):
        asyncio.create_task(incorrect_user_argument(message, state, error_message))
        return

    # it is all correct
    await state.update_data(default_payment=user_default_payment)
    add_menu_message = await message.answer(f'Default payment was recorded: {user_default_payment}')
    asyncio.create_task(write_new_user_argument(message, add_menu_message, state))


async def add_new_user_controller(call: CallbackQuery, state: FSMContext):
    error_message = ''
    state_data = await state.get_data()
    user_id = state_data.get('user_id')
    user_name = state_data.get('user_name')
    default_payment = state_data.get('default_payment')

    await call.answer()

    if user_id is None:
        error_message += 'User ID was not given.'
    if user_name is None:
        error_message += 'User name was not given.'
    if default_payment is None:
        error_message += 'Default payment was not given.'
    if error_message != '':
        await call.message.answer(error_message)

    user = User.get_or_none(User.id == user_id)

    if user is not None:
        error_message += 'This user is exist'

    if error_message != '':
        await call.message.answer(error_message)
        asyncio.create_task(delete_message(call.message))

    try:
        User.create(id=user_id, name=user_name, default_payment=default_payment)
        message_answer = await call.message.answer(
            f'<i>You added new user.</i>\r\n ID: {user_id}\r\n Name: {user_name}\r\n '
            f'Default payment: {default_payment}')
        asyncio.create_task(delete_message(message_answer, 10))
    except Exception:
        error_message = "An error occurred user was not added"
        message_answer = await call.message.answer(error_message)
        asyncio.create_task(delete_message(message_answer, 10))
    finally:
        await call.answer()
        await state.clear()
        message = call.message
        return message
        # await state.set_state(UserOptionsFSM.state_user_options_menu_open)
        # await call.message.answer('User options', reply_markup=get_user_options_menu())
        # asyncio.create_task(delete_message(call.message))
