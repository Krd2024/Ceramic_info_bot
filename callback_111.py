from aiogram import F
import asyncio
from aiogram import types, Dispatcher
from decouple import config
from wrapper_bot import TelegramBotWrapper
from utils import *
from wrapper_bot import TelegramBotWrapper
from aiogram import Dispatcher, types

# from aiogram.types import Message, BotCommand


# from aiogram.types import Message, BotCommand


from decouple import config


TOKEN = config("TOKEN", cast=str, default="пусто")
bot = TelegramBotWrapper(TOKEN)
dp = Dispatcher()


# @dp.message(F.text.startswith("Пл"))
# async def with_puree(message: types.Message):
#     await message.reply("Плитка!")


# @dp.message(F.text.startswith("Ги"))
# async def without_puree(message: types.Message):
#     await message.reply("Гипсокартон!")
