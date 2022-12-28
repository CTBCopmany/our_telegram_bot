from aiogram import types
from aiogram.utils import executor
from control_data import UserData

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot, dp
from main_user_logic import menu_main_admin


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello Text")
    user_data = UserData.user_db()

    if not user_data.check_user(message.from_user.id):
        user_data.add_user(message.from_user.id,
                           message.from_user.username,
                           message.from_user.full_name)


@dp.message_handler(commands=['menu'])
async def process_start_command(message: types.Message):
    privilege = UserData.get_all_privilege_user(message.from_user.id)

    if privilege.count(True) > 0:
        inline_user_choice = InlineKeyboardMarkup()
        if privilege[0]:
            inline_user_choice.add(InlineKeyboardButton("Главный админ", callback_data="user_main_admin"))
        if privilege[1]:
            inline_user_choice.add(InlineKeyboardButton("Админ", callback_data="user_admin"))
        if privilege[2]:
            inline_user_choice.add(InlineKeyboardButton("Менеджер", callback_data="user_manager"))

        await message.reply("Выберите пользователя", reply_markup=inline_user_choice)


@dp.callback_query_handler(lambda c: c.data[:4] == 'user')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if callback_query.data == "user_main_admin":
        await menu_main_admin(callback_query)


if __name__ == '__main__':
    executor.start_polling(dp)
