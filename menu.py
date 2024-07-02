import asyncio
from aiogram import types, Dispatcher, Router
from aiogram.types import Message, BotCommand, InputFile, CallbackQuery
from aiogram.filters import Command
from aiogram import F
from utils import add_user_to_db
from aiogram.types import (
    Message,
    InputMediaPhoto,
    InputMedia,
    ContentType,
    InputMediaAnimation,
)

# from aiogram.dispatcher import Dispatcher
from decouple import config
from wrapper_bot import TelegramBotWrapper
from utils import add_user_to_db

# from utils import *
from wrapper_bot import TelegramBotWrapper
from aiogram import Dispatcher, types

# from aiogram import MemoryStorage
from decouple import config
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.types import FSInputFile, URLInputFile

from aiogram.methods.edit_message_media import EditMessageMedia


async def main_menu(message: Message, callback=None):
    """Главное меню"""

    print("Пришло в main_menu")
    try:

        id_ = message.message_id
        kb = [
            [
                types.KeyboardButton(text="👉 Стоимость работ по укладки плитки* "),
                types.KeyboardButton(text="👉 Гипсокартон"),
                types.KeyboardButton(text=f"📝 Оствить заявку"),
            ]
        ]

        keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
            # one_time_keyboard=True,
            input_field_placeholder="Выберите вид работ",
        )
        if callback is None:
            await message.answer(
                "Привет, ваш пользователь добавлен в базу данных!",
                reply_markup=keyboard,
            )
            return

        return
    except Exception as e:
        print(e, "< --- def main_menu")

        # await message.answer(
        #     "Привет,  Как подавать котлеты?",
        #     reply_markup=keyboard,
        # )
