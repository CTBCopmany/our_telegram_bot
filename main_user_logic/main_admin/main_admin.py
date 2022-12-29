from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

from config import bot, dp
from . import add_new_users
from . import delete_users


#############################################################
#                         MENU                              #
#############################################################
async def menu_main_admin(callback_query: types.CallbackQuery):
    inline_menu_main_admin = InlineKeyboardMarkup()

    inline_menu_main_admin.add(InlineKeyboardButton("Админы", callback_data="menu_main_admin_admin"))
    inline_menu_main_admin.add(InlineKeyboardButton("Менеджеры", callback_data="menu_main_admin_manager"))
    inline_menu_main_admin.add(InlineKeyboardButton("События", callback_data="menu_main_admin_event"))

    await bot.send_message(callback_query.from_user.id, "Меню", reply_markup=inline_menu_main_admin)


#############################################################
#                 Work with menu main admin                 #
#############################################################
@dp.callback_query_handler(lambda c: c.data[:15] == 'menu_main_admin')
async def work_with_menu_main_admin(callback_query: types.CallbackQuery):
    inline_action_main_admin_menu = InlineKeyboardMarkup()

    if callback_query.data == "menu_main_admin_admin":
        inline_action_main_admin_menu.add(InlineKeyboardButton("Добавить",
                                                               callback_data="add_admin_main_admin"))

        inline_action_main_admin_menu.add(InlineKeyboardButton("Удалить",
                                                               callback_data="delete_admin_main_admin"))

        inline_action_main_admin_menu.add(InlineKeyboardButton("Получить всех админов",
                                                               callback_data="get_all_admin_main_admin"))

        inline_action_main_admin_menu.add(InlineKeyboardButton("Найти",
                                                               callback_data="find_admin_main_admin"))

    elif callback_query.data == "menu_main_admin_manager":
        inline_action_main_admin_menu.add(InlineKeyboardButton("Добавить",
                                                               callback_data="add_manager_main_admin"))

        inline_action_main_admin_menu.add(InlineKeyboardButton("Удалить",
                                                               callback_data="delete_manager_main_admin"))

        inline_action_main_admin_menu.add(InlineKeyboardButton("Получить всех менеджеров",
                                                               callback_data="get_all_manager_main_admin"))

        inline_action_main_admin_menu.add(InlineKeyboardButton("Найти",
                                                               callback_data="find_manager_main_admin"))

    else:
        inline_action_main_admin_menu.add(InlineKeyboardButton("Добавить",
                                                               callback_data="add_event_main_admin"))

        inline_action_main_admin_menu.add(InlineKeyboardButton("Удалить",
                                                               callback_data="delete_event_main_admin"))

        inline_action_main_admin_menu.add(InlineKeyboardButton("Получить все события",
                                                               callback_data="get_all_event_main_admin"))

        inline_action_main_admin_menu.add(InlineKeyboardButton("Все события",
                                                               callback_data="get_all_event_main_admin"))

    await bot.send_message(callback_query.from_user.id, "Выберите дейстие", reply_markup=inline_action_main_admin_menu)


#############################################################
#                     Add new users                         #
#############################################################
@dp.callback_query_handler(lambda c: c.data[:3] == "add" and c.data[-10:] == "main_admin")
async def start_add_users_main_admin(callback_query: types.CallbackQuery):
    await add_new_users.start_add_users_main_admin(callback_query)


#############################################################
#                      Delete users                         #
#############################################################
@dp.callback_query_handler(lambda c: c.data[:6] == "delete" and c.data[-10:] == "main_admin")
async def start_delete_admin_main_admin(callback_query: types.CallbackQuery):
    await delete_users.start_delete_admin_main_admin(callback_query)
