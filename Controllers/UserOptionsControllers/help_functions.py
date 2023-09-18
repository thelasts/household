import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup

from Utils.FSM.UserOptions.UserOptionsFSM import UserOptionsFSM
from Utils.Keyboards.Inline.UserOptions.user_options_keyboards import get_user_add_menu, get_user_cancel_menu, \
    get_user_options_menu, get_user_change_menu


async def delete_message(message, time: int = 0):
    await asyncio.sleep(time)
    try:
        await message.delete()
    except Exception as e:
        pass


async def delete_menu_message(state: FSMContext):
    state_data = await state.get_data()
    old_message = state_data.get('old_message')
    if old_message is not None:
        asyncio.create_task(delete_message(old_message))
        await state.update_data(old_message=None)


async def write_new_user_argument(message: Message, info_message: Message, state: FSMContext):
    message_text = 'Add user menu'
    keyboard = get_user_add_menu()
    new_state = UserOptionsFSM.state_open_add_user_menu
    await write_user_argument(message, info_message, state, message_text, keyboard, new_state)


async def write_change_user_argument(message: Message, info_message: Message, state: FSMContext):
    message_text = 'User change menu'
    keyboard = get_user_change_menu()
    new_state = UserOptionsFSM.state_open_change_menu
    await write_user_argument(message, info_message, state, message_text, keyboard, new_state)


async def write_user_argument(message: Message, info_message: Message, state: FSMContext, message_text, keyboard,
                              new_state):
    await message.answer(message_text, reply_markup=keyboard)
    await state.set_state(new_state)
    asyncio.create_task(delete_message(message))
    asyncio.create_task(delete_message(info_message, 10))


async def incorrect_user_argument(message: Message, state: FSMContext, error_message: str):
    asyncio.create_task(delete_message(message))
    menu_message = message.answer(error_message, reply_markup=get_user_cancel_menu())
    await state.update_data(old_message=menu_message)


async def send_submenu_to_callback(message_text: str, keyboard: InlineKeyboardMarkup, state: FSMContext,
                                   call: CallbackQuery):
    await call.answer()
    await state.update_data(old_message=None)
    menu_message = await call.message.answer(message_text, reply_markup=keyboard)
    asyncio.create_task(delete_message(call.message))

    return menu_message


async def send_cancel_menu_to_callback(message_text: str, state: FSMContext,
                                       call: CallbackQuery):
    keyboard = get_user_cancel_menu()
    menu_message = await send_submenu_to_callback(message_text, keyboard, state, call)
    await state.update_data(old_message=menu_message)


async def request_message(message_text: str, call: CallbackQuery, state: FSMContext, new_state):
    await state.set_state(new_state)
    await send_cancel_menu_to_callback(message_text, state, call)


async def get_user_id(error_message: str, message: Message) -> tuple[int | None, str]:
    user_id = None

    # check message is contact or id number
    if message.contact is not None:
        try:
            user_id = int(message.contact.user_id)
        except (ValueError, TypeError):
            error_message = 'You sent a contact that is not in the telegram. ' + error_message
            user_id = None
    else:
        try:
            user_id = int(message.text)
        except (ValueError, TypeError):
            user_id = None
            error_message = 'You entered invalid id. ' + error_message
    return user_id, error_message


async def get_user_name(message: Message):
    error_message = ''
    user_name = message.text

    if user_name is None:
        error_message = 'Invalid name format.Write username'

    return user_name, error_message


async def get_default_payment(message: Message):
    user_default_payment = None
    error_message = 'Invalid default payment format. Write number'

    try:
        user_default_payment = int(message.text)
    except (ValueError, TypeError):
        user_default_payment = None

    return user_default_payment, error_message
