from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    wait_minus_balance = State()
    wait_id = State()
    wait_message = State()
    wait_change_balance = State()
    wait_add_balance = State()
    logs_history = State()
    has_mail_check = State()
    link_to_lzt = State()

