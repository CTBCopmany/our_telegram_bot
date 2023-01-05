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

    class Event(StatesGroup):
        ADD_EVENT_TEXT_MAIN_ADMIN = State()
        ADD_EVENT_IMG_MAIN_ADMIN = State()
        DELETE_EVENT_MAIN_ADMIN = State()
