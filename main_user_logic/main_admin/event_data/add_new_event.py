from config import bot, dp
from aiogram import types
from .control_event_data import EventData
from aiogram.dispatcher import FSMContext
from .utils import Event
from control_data import UserData


async def add_new_event_start(callback_query: types.CallbackQuery) -> None:
    await bot.send_message(callback_query.from_user.id, "Отправте обложку")
    await Event.ADD_EVENT_IMG_MAIN_ADMIN.set()


@dp.message_handler(lambda message: not message.photo, state=Event.ADD_EVENT_IMG_MAIN_ADMIN)
async def check_photo_for_event(message: types.Message):
    await message.reply("Это не фото")


@dp.message_handler(lambda message: message.photo, state=Event.ADD_EVENT_IMG_MAIN_ADMIN, content_types=["photo"])
async def add_photo_event(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id

    await message.reply("Отправте текст")

    await Event.ADD_EVENT_TEXT_MAIN_ADMIN.set()


@dp.message_handler(state=Event.ADD_EVENT_TEXT_MAIN_ADMIN)
async def add_text_event(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["text"] = message.text

    async with state.proxy() as data:
        event = EventData()
        event.add_event(data["text"], data["photo"])

        await message.reply("Событие добавлена")
        await bot.send_photo(chat_id=message.from_user.id, photo=data["photo"], caption=data["text"])

        for users in UserData.user_db().get_all_user():
            await bot.send_photo(chat_id=users[0], photo=data["photo"], caption=data["text"])

    await state.finish()
