from aiogram import F
from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from Controllers.UserOptionsControllers.user_options_controller import open_user_option_menu_controller, \
    close_user_option_menu_controller, open_user_add_menu_controller, request_change_user_id_controller
from Utils.FSM.UserOptions.UserOptionsFSM import UserOptionsFSM

user_operations_router = Router(name="user_operations")


@user_operations_router.message(Command("user_options"))
async def open_user_options_menu_router(message: Message, state: FSMContext):
    await open_user_option_menu_controller(message, state)


@user_operations_router.callback_query(UserOptionsFSM.state_user_options_menu_open, F.data == 'CANCEL')
async def close_user_options_menu_router(call: CallbackQuery, state: FSMContext):
    await close_user_option_menu_controller(call, state)


@user_operations_router.callback_query(UserOptionsFSM.state_user_options_menu_open, F.data == 'ADD_USER')
async def open_user_add_menu_router(call: CallbackQuery, state: FSMContext):
    await open_user_add_menu_controller(call, state)


@user_operations_router.callback_query(UserOptionsFSM.state_user_options_menu_open, F.data == 'CHANGE_USER')
async def request_change_user_id_router(call: CallbackQuery, state: FSMContext):
    await request_change_user_id_controller(call, state)
