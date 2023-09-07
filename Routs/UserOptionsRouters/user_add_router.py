from aiogram import F
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from Controllers.UserOptionsControllers.user_add_controller import (
    request_user_id_controller,
    request_user_name_controller,
    request_default_payment_controller,
    add_new_user_controller,
    add_user_id_controller,
    add_user_name_controller,
    add_user_default_payment_controller, main_cancel_controller)
from Controllers.UserOptionsControllers.user_options_controller import open_user_add_menu_controller, \
    open_user_option_menu_controller
from Utils.FSM.UserOptions.UserOptionsFSM import UserOptionsFSM

user_add_router = Router(name='user_add_router')


@user_add_router.callback_query(UserOptionsFSM.state_open_add_user_menu, F.data == 'ADD_ID')
async def request_user_id_router(call: CallbackQuery, state: FSMContext):
    await request_user_id_controller(call, state)


@user_add_router.callback_query(UserOptionsFSM.state_open_add_user_menu, F.data == 'ADD_NAME')
async def request_user_name_router(call: CallbackQuery, state: FSMContext):
    await request_user_name_controller(call, state)


@user_add_router.callback_query(UserOptionsFSM.state_open_add_user_menu, F.data == 'ADD_DEF_PAY')
async def request_user_default_payment_router(call: CallbackQuery, state: FSMContext):
    await request_default_payment_controller(call, state)


@user_add_router.callback_query(UserOptionsFSM.state_open_add_user_menu, F.data == 'DONE')
async def add_new_user_router(call: CallbackQuery, state: FSMContext):
    message = await add_new_user_controller(call, state)
    await open_user_option_menu_controller(message, state)


@user_add_router.callback_query(UserOptionsFSM.state_open_add_user_menu, F.data == 'CANCEL')
async def main_cancel_router(call: CallbackQuery, state: FSMContext):
    message = await main_cancel_controller(call, state)
    await open_user_option_menu_controller(message, state)


@user_add_router.callback_query(UserOptionsFSM.state_add_new_user_id, F.data == 'CANCEL')
async def cancel_router(call: CallbackQuery, state: FSMContext):
    await open_user_add_menu_controller(call, state)


@user_add_router.callback_query(UserOptionsFSM.state_add_new_user_name, F.data == 'CANCEL')
async def cancel_router(call: CallbackQuery, state: FSMContext):
    await open_user_add_menu_controller(call, state)


@user_add_router.callback_query(UserOptionsFSM.state_add_new_user_default_payment, F.data == 'CANCEL')
async def cancel_router(call: CallbackQuery, state: FSMContext):
    await open_user_add_menu_controller(call, state)


@user_add_router.message(UserOptionsFSM.state_add_new_user_id)
async def add_user_id_router(message: Message, state: FSMContext):
    await add_user_id_controller(message, state)


@user_add_router.message(UserOptionsFSM.state_add_new_user_name)
async def add_user_name_router(message: Message, state: FSMContext):
    await add_user_name_controller(message, state)


@user_add_router.message(UserOptionsFSM.state_add_new_user_default_payment)
async def add_user_default_payment_router(message: Message, state: FSMContext):
    await add_user_default_payment_controller(message, state)
