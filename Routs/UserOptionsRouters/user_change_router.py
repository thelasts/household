from aiogram import F
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from Controllers.UserOptionsControllers.user_change_controller import check_user_id_controller, \
    request_user_name_controller, request_user_default_payment_controller, change_user_name_controller, \
    change_default_payment_controller, open_change_user_menu_controller, change_user_controller, main_cancel_controller
from Controllers.UserOptionsControllers.user_options_controller import open_user_option_menu_controller
from Utils.FSM.UserOptions.UserOptionsFSM import UserOptionsFSM

user_change_router = Router(name='user_change_router')


@user_change_router.message(UserOptionsFSM.state_wait_contact_for_change)
async def check_user_id_router(message: Message, state: FSMContext):
    back_to_menu = await check_user_id_controller(message, state)
    if back_to_menu:
        await open_user_option_menu_controller(message, state)
    else:
        await open_change_user_menu_controller(message, state)


@user_change_router.callback_query(UserOptionsFSM.state_open_change_menu, F.data == 'CHANGE_NAME')
async def request_user_name_router(call: CallbackQuery, state: FSMContext):
    await request_user_name_controller(call, state)


@user_change_router.callback_query(UserOptionsFSM.state_open_change_menu, F.data == 'CHANGE_DEF_PAY')
async def request_user_default_payment_router(call: CallbackQuery, state: FSMContext):
    await request_user_default_payment_controller(call, state)


@user_change_router.message(UserOptionsFSM.state_change_name)
async def change_user_name_router(message: Message, state: FSMContext):
    await change_user_name_controller(message, state)


@user_change_router.message(UserOptionsFSM.state_change_default_payment)
async def change_default_payment_router(message: Message, state: FSMContext):
    await change_default_payment_controller(message, state)


@user_change_router.callback_query(UserOptionsFSM.state_open_change_menu, F.data == 'DONE')
async def change_user_router(call: CallbackQuery, state: FSMContext):
    message = await change_user_controller(call, state)
    await open_user_option_menu_controller(message, state)


@user_change_router.callback_query(UserOptionsFSM.state_open_change_menu, F.data == 'CANCEL')
async def main_cancel_router(call: CallbackQuery, state: FSMContext):
    message = await main_cancel_controller(call, state)
    await open_user_option_menu_controller(message, state)


@user_change_router.callback_query(UserOptionsFSM.state_change_name, F.data == 'CANCEL')
async def cancel_router(call: CallbackQuery, state: FSMContext):
    await open_change_user_menu_controller(call, state)


@user_change_router.callback_query(UserOptionsFSM.state_change_default_payment, F.data == 'CANCEL')
async def cancel_router(call: CallbackQuery, state: FSMContext):
    await open_change_user_menu_controller(call, state)


@user_change_router.callback_query(UserOptionsFSM.state_wait_contact_for_change, F.data == 'CANCEL')
async def cancel_router(call: CallbackQuery, state: FSMContext):
    message = await main_cancel_controller(call, state)
    await open_user_option_menu_controller(message, state)
