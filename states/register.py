from aiogram.fsm.state import State, StatesGroup


class RegisterState(StatesGroup):
    first_name = State()
    last_name = State()
    phone = State()
    province = State()
    job = State()
    activity = State()