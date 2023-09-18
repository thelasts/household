from aiogram.fsm.state import StatesGroup, State


class UserOptionsFSM(StatesGroup):
    # States for designations that users option is open
    state_user_options_menu_open = State()

    # States for add new user
    state_open_add_user_menu = State()
    state_add_new_user_id = State()
    state_add_new_user_name = State()
    state_add_new_user_default_payment = State()

    # States for delete users
    state_wait_contact_for_delete = State()

    # States for changes users
    state_open_change_menu = State()
    state_wait_contact_for_change = State()
    state_change_name = State()
    state_change_default_payment = State()