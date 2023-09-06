from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from Utils.Keyboards.Inline.UserOptions.const import BUTTONS_IN_FIRST_LINE, USER_OPTIONS_MENU_BUTTONS, \
    USER_ADD_MENU_BUTTONS, USER_CANCEL_MENU, USER_CHANGE_MENU


def add_new_buttons(buttons: dict, keyboard_builder: InlineKeyboardBuilder):
    for text, call_data in buttons.items():
        keyboard_builder.button(text=text, callback_data=call_data)
    keyboard_builder.adjust(BUTTONS_IN_FIRST_LINE)


def get_user_options_menu() -> InlineKeyboardMarkup:
    keyboard_builder = InlineKeyboardBuilder()
    add_new_buttons(USER_OPTIONS_MENU_BUTTONS, keyboard_builder)
    return keyboard_builder.as_markup()


def get_user_add_menu() -> InlineKeyboardMarkup:
    keyboard_builder = InlineKeyboardBuilder()
    add_new_buttons(USER_ADD_MENU_BUTTONS, keyboard_builder)
    return keyboard_builder.as_markup()


def get_user_cancel_menu() -> InlineKeyboardMarkup:
    keyboard_builder = InlineKeyboardBuilder()
    add_new_buttons(USER_CANCEL_MENU, keyboard_builder)
    return keyboard_builder.as_markup()


def get_user_change_menu() -> InlineKeyboardMarkup:
    keyboard_builder = InlineKeyboardBuilder()
    add_new_buttons(USER_CHANGE_MENU, keyboard_builder)
    return keyboard_builder.as_markup()
