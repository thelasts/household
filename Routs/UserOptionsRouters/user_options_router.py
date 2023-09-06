from aiogram import F
from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from Controllers.UserOptionsControllers.user_options_controller import open_user_option_menu_controller, \
    close_user_option_menu_controller, open_user_add_menu_controller
from Utils.FSM.UserOptions.UserOptionsFSM import UserOptionsFSM

user_operations_router = Router(name="user_operations")


@user_operations_router.message(Command("user_options"))
async def get_user_options_menu(message: Message, state: FSMContext):
    await open_user_option_menu_controller(message, state)


@user_operations_router.callback_query(UserOptionsFSM.state_user_options_menu_open, F.data == 'CANCEL')
async def close_user_options_menu(call: CallbackQuery, state: FSMContext):
    await close_user_option_menu_controller(call, state)


@user_operations_router.callback_query(UserOptionsFSM.state_user_options_menu_open, F.data == 'ADD_USER')
async def get_user_add_menu(call: CallbackQuery, state: FSMContext):
    await open_user_add_menu_controller(call, state)
