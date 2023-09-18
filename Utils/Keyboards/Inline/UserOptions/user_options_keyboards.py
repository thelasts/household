from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from Utils.Keyboards.Inline.UserOptions.const import USER_OPTIONS_MENU_BUTTONS, \
    USER_ADD_MENU_BUTTONS, USER_CANCEL_MENU, USER_CHANGE_MENU, BUTTONS_IN_FIRST_LINE_OPTIONS_MENU, \
    BUTTONS_IN_FIRST_LINE_ADD_MENU, BUTTONS_IN_FIRST_LINE_CHANGE_MENU


def add_new_buttons(buttons: dict, keyboard_builder: InlineKeyboardBuilder, button_in_first_line):
    for text, call_data in buttons.items():
        keyboard_builder.button(text=text, callback_data=call_data)
    keyboard_builder.adjust(button_in_first_line)


def get_user_options_menu() -> InlineKeyboardMarkup:
    keyboard_builder = InlineKeyboardBuilder()
    add_new_buttons(USER_OPTIONS_MENU_BUTTONS, keyboard_builder, BUTTONS_IN_FIRST_LINE_OPTIONS_MENU)
    return keyboard_builder.as_markup()


def get_user_add_menu() -> InlineKeyboardMarkup:
    keyboard_builder = InlineKeyboardBuilder()
    add_new_buttons(USER_ADD_MENU_BUTTONS, keyboard_builder, BUTTONS_IN_FIRST_LINE_ADD_MENU)
    return keyboard_builder.as_markup()


def get_user_cancel_menu() -> InlineKeyboardMarkup:
    buttons_in_first_line = 1
    keyboard_builder = InlineKeyboardBuilder()
    add_new_buttons(USER_CANCEL_MENU, keyboard_builder, buttons_in_first_line)
    return keyboard_builder.as_markup()


def get_user_change_menu() -> InlineKeyboardMarkup:
    keyboard_builder = InlineKeyboardBuilder()
    add_new_buttons(USER_CHANGE_MENU, keyboard_builder, BUTTONS_IN_FIRST_LINE_CHANGE_MENU)
    return keyboard_builder.as_markup()
