from config import bot, dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types


async def menu_main_admin(callback_query: types.CallbackQuery):
    inline_menu_main_admin = InlineKeyboardMarkup()

    inline_menu_main_admin.add(InlineKeyboardButton("Админы", callback_data="menu_main_admin_admin"))
    inline_menu_main_admin.add(InlineKeyboardButton("Менеджеры", callback_data="menu_main_admin_manager"))
    inline_menu_main_admin.add(InlineKeyboardButton("События", callback_data="menu_main_admin_event"))

    await bot.send_message(callback_query.from_user.id, "Меню", reply_markup=inline_menu_main_admin)


@dp.callback_query_handler(lambda c: c.data[:15] == 'menu_main_admin')
async def process_callback_button1(callback_query: types.CallbackQuery):
    print(callback_query.data)
