from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

from config import bot, dp
from control_data import UserData
from . import add_new_users
from . import delete_users
from .event_data import add_new_event, delete_event


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
    await callback_query.message.delete()

    inline_action_main_admin_menu = InlineKeyboardMarkup()

    if callback_query.data == "menu_main_admin_admin":
        inline_action_main_admin_menu.add(InlineKeyboardButton("Добавить",
                                                               callback_data="add_admin_main_admin"))

        inline_action_main_admin_menu.add(InlineKeyboardButton("Удалить",
                                                               callback_data="delete_admin_main_admin"))

        inline_action_main_admin_menu.add(InlineKeyboardButton("Получить всех админов",
                                                               callback_data="get_all_admin_main_admin"))

    elif callback_query.data == "menu_main_admin_manager":
        inline_action_main_admin_menu.add(InlineKeyboardButton("Добавить",
                                                               callback_data="add_manager_main_admin"))

        inline_action_main_admin_menu.add(InlineKeyboardButton("Удалить",
                                                               callback_data="delete_manager_main_admin"))

        inline_action_main_admin_menu.add(InlineKeyboardButton("Получить всех менеджеров",
                                                               callback_data="get_all_manager_main_admin"))

    else:
        inline_action_main_admin_menu.add(InlineKeyboardButton("Добавить",
                                                               callback_data="add_event_main_admin"))

        inline_action_main_admin_menu.add(InlineKeyboardButton("Удалить",
                                                               callback_data="delete_event_main_admin"))

    await bot.send_message(callback_query.from_user.id, "Выберите дейстие", reply_markup=inline_action_main_admin_menu)


#############################################################
#                           Add                             #
#############################################################
@dp.callback_query_handler(lambda c: c.data[:3] == "add" and c.data[-10:] == "main_admin")
async def start_add_main_admin(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    if callback_query.data == "add_event_main_admin":
        await add_new_event.add_new_event_start(callback_query)
    else:
        await add_new_users.start_add_users_main_admin(callback_query)


#############################################################
#                          Delete                           #
#############################################################
@dp.callback_query_handler(lambda c: c.data[:6] == "delete" and c.data[-10:] == "main_admin")
async def start_delete_main_admin(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    if callback_query.data == "delete_event_main_admin":
        await delete_event.delete_event_menu_main_admin(callback_query)
    else:
        await delete_users.start_delete_admin_main_admin(callback_query)


#############################################################
#                 Get all users or event                    #
#############################################################
@dp.callback_query_handler(lambda c: c.data[:7] == "get_all" and c.data[-10:] == "main_admin")
async def get_all_user(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    if callback_query.data == "get_all_event_main_admin":
        pass

    else:
        table_all_admin = "id || username || full name \n"

        if callback_query.data == "get_all_admin_main_admin":
            for i in UserData.admin_db().get_all_user():
                table_all_admin += str(i[0]) + " || " + str(i[1]) + " || " + i[2] + "\n"

        if callback_query.data == "get_all_manager_main_admin":
            for i in UserData.main_admin_db().get_all_user():
                table_all_admin += str(i[0]) + " || " + str(i[1]) + " || " + i[2] + "\n"

        await bot.send_message(callback_query.from_user.id, table_all_admin)
