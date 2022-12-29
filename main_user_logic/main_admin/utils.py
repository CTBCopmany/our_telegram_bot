from aiogram.dispatcher.filters.state import StatesGroup, State


class WorkWithUserMainAdmin:
    class Admin(StatesGroup):
        ADD_USER_MAIN_ADMIN_STATES = State()
        DELETE_USER_MAIN_ADMIN_STATES = State()
        FIND_USER_MAIN_ADMIN_STATES = State()

    class Manager(StatesGroup):
        ADD_USER_MAIN_ADMIN_STATES = State()
        DELETE_USER_MAIN_ADMIN_STATES = State()
        FIND_USER_MAIN_ADMIN_STATES = State()
