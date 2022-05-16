from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

storage = MemoryStorage()

load_dotenv(".env")

bot = Bot(token=os.environ.get('TOKEN'))
dp = Dispatcher(bot, storage=storage)
