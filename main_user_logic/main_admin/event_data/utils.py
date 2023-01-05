from aiogram.dispatcher.filters.state import StatesGroup, State


class Event(StatesGroup):
    ADD_EVENT_TEXT_MAIN_ADMIN = State()
    ADD_EVENT_IMG_MAIN_ADMIN = State()
