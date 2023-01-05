from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from pathlib import Path
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

TOKEN = "Your Token"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

path = Path(__file__).parent

user_data_url = """Your user data url"""
event_data_url = """Your event data url"""
