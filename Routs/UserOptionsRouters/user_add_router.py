from aiogram import F
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from Controllers import (get_wait_user_id_message_controller, get_wait_user_name_message_controller,
                         get_wait_user_default_payment_message_controller, write_new_user_id_controller,
                         write_new_user_name_controller, write_new_user_default_payment_controller,
                         add_new_user_controller)
from Controllers.UserOptionsControllers.user_add_controller import add_new_user_main_cancel_controller, \
    add_new_user_cancel_controller
from Utils.FSM.UserOptions import UserOptionsFSM

user_add_router = Router(name='user_add_router')


@user_add_router.callback_query(UserOptionsFSM.state_open_add_user_menu, F.data == 'ADD_ID')
async def wait_user_id(call: CallbackQuery, state: FSMContext):
    await get_wait_user_id_message_controller(call, state)


@user_add_router.callback_query(UserOptionsFSM.state_open_add_user_menu, F.data == 'ADD_NAME')
async def wait_user_name(call: CallbackQuery, state: FSMContext):
    await get_wait_user_name_message_controller(call, state)


@user_add_router.callback_query(UserOptionsFSM.state_open_add_user_menu, F.data == 'ADD_DEF_PAY')
async def wait_user_default_payment(call: CallbackQuery, state: FSMContext):
    await get_wait_user_default_payment_message_controller(call, state)


@user_add_router.callback_query(UserOptionsFSM.state_open_add_user_menu, F.data == 'DONE')
async def add_new_user(call: CallbackQuery, state: FSMContext):
    await add_new_user_controller(call, state)


@user_add_router.callback_query(UserOptionsFSM.state_open_add_user_menu, F.data == 'CANCEL')
async def add_new_user(call: CallbackQuery, state: FSMContext):
    await add_new_user_main_cancel_controller(call, state)


@user_add_router.callback_query(UserOptionsFSM.state_add_new_user_id, F.data == 'CANCEL')
async def add_new_user(call: CallbackQuery, state: FSMContext):
    await add_new_user_cancel_controller(call, state)


@user_add_router.callback_query(UserOptionsFSM.state_add_new_user_name, F.data == 'CANCEL')
async def add_new_user(call: CallbackQuery, state: FSMContext):
    await add_new_user_cancel_controller(call, state)


@user_add_router.callback_query(UserOptionsFSM.state_add_new_user_default_payment, F.data == 'CANCEL')
async def add_new_user(call: CallbackQuery, state: FSMContext):
    await add_new_user_cancel_controller(call, state)


@user_add_router.message(UserOptionsFSM.state_add_new_user_id)
async def add_user_id(message: Message, state: FSMContext):
    await write_new_user_id_controller(message, state)


@user_add_router.message(UserOptionsFSM.state_add_new_user_name)
async def add_user_name(message: Message, state: FSMContext):
    await write_new_user_name_controller(message, state)


@user_add_router.message(UserOptionsFSM.state_add_new_user_default_payment)
async def add_user_default_payment(message: Message, state: FSMContext):
    await write_new_user_default_payment_controller(message, state)
