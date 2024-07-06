import asyncio
from decouple import config
from wrapper_bot import TelegramBotWrapper
from utils import *
from aiogram import Dispatcher
from callback import main


TOKEN = config("TOKEN", cast=str, default="пусто")
bot = TelegramBotWrapper(TOKEN)
dp = Dispatcher()

if __name__ == "__main__":
    asyncio.run(main())
