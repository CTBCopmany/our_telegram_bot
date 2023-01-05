from config import bot, dp
from aiogram import types
from control_data import UserData
from aiogram.dispatcher import FSMContext
from .utils import WorkWithUserMainAdmin


@dp.message_handler(commands=['cansel'], state='*')
async def cansel_add_new_event(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return None

    await message.reply("Отменена")

    await state.finish()


async def start_delete_admin_main_admin(callback_query: types.CallbackQuery):
    if callback_query.data == "delete_admin_main_admin":
        await bot.send_message(callback_query.from_user.id, "Введите id")
        await WorkWithUserMainAdmin.Admin.DELETE_USER_MAIN_ADMIN_STATES.set()

    elif callback_query.data == "delete_manager_main_admin":
        await bot.send_message(callback_query.from_user.id, "Введите id")
        await WorkWithUserMainAdmin.Manager.DELETE_USER_MAIN_ADMIN_STATES.set()


@dp.message_handler(state=WorkWithUserMainAdmin.Admin.DELETE_USER_MAIN_ADMIN_STATES)
async def delete_admin_main_admin(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        user_id = int(message.text)
        admin = UserData.admin_db()

        if admin.check_user(user_id):
            admin.delete_user(user_id)

            await message.reply("Админ удален успешно")

        else:
            await message.reply("Этого админа не существует")
    else:
        await message.reply("Вы неправильно вели id")

    await state.finish()


@dp.message_handler(state=WorkWithUserMainAdmin.Manager.DELETE_USER_MAIN_ADMIN_STATES)
async def delete_admin_main_admin(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        user_id = int(message.text)
        manager = UserData.manager_db()

        if manager.check_user(user_id):
            manager.delete_user(user_id)

            await message.reply("Менеджер удален успешно")

        else:
            await message.reply("Этого менеджера не существует")
    else:
        await message.reply("Вы неправильно вели id")

    await state.finish()
