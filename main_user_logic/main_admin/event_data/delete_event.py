from config import bot, dp
from aiogram import types
from .control_event_data import EventData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def delete_event_menu_main_admin(callback_query: types.CallbackQuery):
    event = EventData()
    amount_event = len(event.get_all_event())

    if amount_event > 1:
        inline_delete_event_menu = InlineKeyboardMarkup(row_width=2)

        inline_delete_event_menu.row(InlineKeyboardButton("Удалить", callback_data="delete_delete_event_id_0"),
                                     InlineKeyboardButton("Следующий", callback_data="delete_next_event_id_0"))

        first_event = event.get_all_event()[0]
        await bot.send_photo(chat_id=callback_query.from_user.id,
                             photo=first_event[2],
                             caption=first_event[1],
                             reply_markup=inline_delete_event_menu)
    elif amount_event == 1:
        inline_delete_event_menu = InlineKeyboardMarkup()

        inline_delete_event_menu.row(InlineKeyboardButton("Удалить", callback_data="delete_delete_event_id_0"))

        first_event = event.get_all_event()[0]
        await bot.send_photo(chat_id=callback_query.from_user.id,
                             photo=first_event[2],
                             caption=first_event[1],
                             reply_markup=inline_delete_event_menu)

    else:
        await bot.send_message(callback_query.from_user.id, "У вас нету событий")


@dp.callback_query_handler(lambda c: c.data[:22] == "delete_delete_event_id")
async def delete_event_main_admin(callback_query: types.CallbackQuery):
    await callback_query.message.delete()

    event = EventData()
    event_id = event.get_all_event()[int(callback_query.data.split("_")[-1])][0]
    event.delete_event(event_id)

    await bot.send_message(callback_query.from_user.id, "Событие удалена")


@dp.callback_query_handler(lambda c: c.data[:20] == "delete_next_event_id")
async def next_event_main_admin(callback_query: types.CallbackQuery):
    await callback_query.message.delete()

    event = EventData()
    this_event_id = int(callback_query.data.split("_")[-1]) + 1
    all_event = event.get_all_event()
    amount_event = len(all_event)

    if amount_event - 1 > this_event_id:
        inline_menu_event_delete = InlineKeyboardMarkup(row_width=3)
        inline_menu_event_delete.row(
            InlineKeyboardButton("Предедущий", callback_data=f"delete_before_event_id_{this_event_id}"),
            InlineKeyboardButton("Удалить", callback_data=f"delete_delete_event_id_{this_event_id}"),
            InlineKeyboardButton("Следующий", callback_data=f"delete_next_event_id_{this_event_id}"))

    else:
        inline_menu_event_delete = InlineKeyboardMarkup(row_width=2)
        inline_menu_event_delete.row(
            InlineKeyboardButton("Предедущий", callback_data=f"delete_before_event_id_{this_event_id}"),
            InlineKeyboardButton("Удалить", callback_data=f"delete_delete_event_id_{this_event_id}"))

    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo=all_event[this_event_id][2],
                         caption=all_event[this_event_id][1],
                         reply_markup=inline_menu_event_delete)


@dp.callback_query_handler(lambda c: c.data[:22] == "delete_before_event_id")
async def before_event_main_admin(callback_query: types.CallbackQuery):
    await callback_query.message.delete()

    event = EventData()
    this_event_id = int(callback_query.data.split("_")[-1]) - 1
    all_event = event.get_all_event()

    if this_event_id != 0:
        inline_menu_event_delete = InlineKeyboardMarkup(row_width=3)
        inline_menu_event_delete.row(
            InlineKeyboardButton("Предедущий", callback_data=f"delete_before_event_id_{this_event_id}"),
            InlineKeyboardButton("Удалить", callback_data=f"delete_delete_event_id_{this_event_id}"),
            InlineKeyboardButton("Следующий", callback_data=f"delete_next_event_id_{this_event_id}"))

    else:
        inline_menu_event_delete = InlineKeyboardMarkup(row_width=2)
        inline_menu_event_delete.row(
            InlineKeyboardButton("Удалить", callback_data=f"delete_delete_event_id_{this_event_id}"),
            InlineKeyboardButton("Следующий", callback_data=f"delete_next_event_id_{this_event_id}"))

    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo=all_event[this_event_id][2],
                         caption=all_event[this_event_id][1],
                         reply_markup=inline_menu_event_delete)
