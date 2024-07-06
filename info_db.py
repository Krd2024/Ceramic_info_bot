from menu import main_menu
from wrapper_bot import TelegramBotWrapper
from aiogram import types
from aiogram import types
from decouple import config
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import aiosqlite
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from aiogram import types
from img import *
from delete_chat import delete


TOKEN = config("TOKEN", cast=str, default="пусто")
bot = TelegramBotWrapper(TOKEN)
