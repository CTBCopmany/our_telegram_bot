from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from pathlib import Path

TOKEN = "Your token"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

path = Path(__file__).parent
