from aiogram import types
from aiogram.utils import executor

from config import bot, dp


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello Text")

    print(message.from_user.id)  # user id
    print(message.from_user.username)  # username
    print(message.from_user.full_name)  # user full name


if __name__ == '__main__':
    executor.start_polling(dp)
