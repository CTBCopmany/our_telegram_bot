from config import bot, dp
from aiogram import types
from control_data import UserData
from aiogram.dispatcher import FSMContext
from .utils import WorkWithUserMainAdmin


async def start_add_users_main_admin(callback_query: types.CallbackQuery):
    if callback_query.data == "add_admin_main_admin":
        await bot.send_message(callback_query.from_user.id, "Введите id")
        await WorkWithUserMainAdmin.Admin.ADD_USER_MAIN_ADMIN_STATES.set()

    elif callback_query.data == "add_manager_main_admin":
        await bot.send_message(callback_query.from_user.id, "Введите id")
        await WorkWithUserMainAdmin.Manager.ADD_USER_MAIN_ADMIN_STATES.set()


@dp.message_handler(state=WorkWithUserMainAdmin.Admin.ADD_USER_MAIN_ADMIN_STATES)
async def add_users_main_admin(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        user_id = int(message.text)
        user = UserData.user_db()
        admin = UserData.admin_db()
        if user.check_user(user_id) and not admin.check_user(user_id):
            user_information = user.get_all_information_user("user_id", user_id)

            admin.add_user(user_information[0],
                           user_information[1],
                           user_information[2])

            await message.reply("Пользователь успешно добавлен")

        else:
            await message.reply("Польватель не найден или уже добавлен")
    else:
        await message.reply("Вы неправильно вели id")

    await state.finish()


@dp.message_handler(state=WorkWithUserMainAdmin.Manager.ADD_USER_MAIN_ADMIN_STATES)
async def add_users_main_admin(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        user_id = int(message.text)
        user = UserData.user_db()
        manager = UserData.manager_db()
        if user.check_user(user_id) and not manager.check_user(user_id):
            user_information = user.get_all_information_user("user_id", user_id)

            manager.add_user(user_information[0],
                             user_information[1],
                             user_information[2])

            await message.reply("Пользователь успешно добавлен")

        else:
            await message.reply("Польватель не найден или уже добавлен")
    else:
        await message.reply("Вы неправильно вели id")

    await state.finish()
