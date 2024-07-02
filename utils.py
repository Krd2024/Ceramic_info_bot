from wrapper_bot import TelegramBotWrapper
import asyncio
import asyncio
from aiogram import types, Dispatcher, Router
from aiogram.types import Message, BotCommand, InputFile, CallbackQuery
from aiogram.filters import Command
from aiogram import F
from aiogram.types import (
    Message,
    InputMediaPhoto,
    InputMedia,
    ContentType,
    InputMediaAnimation,
)

from decouple import config
from wrapper_bot import TelegramBotWrapper

# from utils import *
from wrapper_bot import TelegramBotWrapper
from aiogram import Dispatcher, types

from decouple import config

from aiogram.types import FSInputFile, URLInputFile

from aiogram.methods.edit_message_media import EditMessageMedia
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import aiosqlite
from aiogram.types import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.types import Message, BotCommand
from aiogram import types

TOKEN = config("TOKEN", cast=str, default="пусто")
bot = TelegramBotWrapper(TOKEN)


# Функция для добавления пользователя в базу данных
# Асинхронная функция для добавления пользователя в базу данных
async def add_user_to_db(user_id, username, first_name, last_name):
    # Устанавливаем соединение с базой данных SQLite
    async with aiosqlite.connect("sqlite.db") as conn:
        # Создаем курсор для выполнения SQL-запросов
        async with conn.cursor() as cursor:
            # Выполняем запрос на вставку данных пользователя
            await cursor.execute(
                """
                INSERT INTO users (user_id, username, first_name, last_name)
                VALUES (?, ?, ?, ?)
                """,
                (user_id, username, first_name, last_name),
            )
            # Коммитим изменения в базу данных
            await conn.commit()


async def gipsokarton_key(message: types.Message):
    builder = ReplyKeyboardBuilder()
    list_products = [
        "Создание каркаса для объёмных конструкций",
        "Выравнивание стен ",
        "Возведение перегородок",
        "Отделка потолков",
    ]
    # for i in range(1, 5):
    for i in list_products:
        builder.add(types.KeyboardButton(text=str(i)))
    builder.adjust(2)

    await message.answer(
        "Выберите:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )


# =================================================================


async def plitka_key(message: types.Message):
    builder = ReplyKeyboardBuilder()
    list_products = [
        "Пол",
        "Стены",
        "Санузел",
        "Объём",
        "📝 Оставить заявку",
        "⬅️ Назад",
    ]
    # for i in range(1, 5):
    for i in list_products:
        builder.add(types.KeyboardButton(text=str(i)))
    builder.adjust(2, 2, 1, 1)
    reply_markup = builder.as_markup(resize_keyboard=True)
    # return reply_markup
    await message.answer(
        "Выберите:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )


async def plitka_key_choice_price(message: types.Message, key=None):
    if key == 1:
        text = f"Укладка пол ...\nЦена от 1800 руб\n"
        media = FSInputFile("plitka_pol.jpg")

    if key == 2:
        text = f"Укладка  санузел...\nЦена от 1800 руб\n"
        media = FSInputFile("plitka_sanuzel.jpeg")
    if key == 3:
        text = f"Укладка объём...\nЦена от 1300 руб\n"
        media = FSInputFile("ob'em.jpg")

    builder = ReplyKeyboardBuilder()

    list_products = ["⬅️ Назад", "📝 Оставить заявку или уточнить детали"]
    # for i in range(1, 5):
    for i in list_products:
        builder.add(types.KeyboardButton(text=str(i)))
    builder.adjust(2)

    print(message.message_id)

    # try:
    #     await bot.edit_message_text(
    #         chat_id=message.chat.id,
    #         message_id=1226,
    #         # reply_markup=builder.as_markup(resize_keyboard=True),
    #         text=f"{text} +",
    #     )
    # except Exception as e:
    #     print(e)

    # await message.reply(
    #     # chat_id=message.chat.id,
    #     # reply_markup=builder.as_markup(resize_keyboard=True),
    #     text=text,
    # )

    # =================================================================
    print(message.chat.id)
    print(message.message_id)

    x = await bot.send_photo(message.chat.id, photo=media)
    print(x.message_id, "< -------- x.message_id ")

    # reply_markup = InlineKeyboardMarkup(
    #     inline_keyboard=[
    #         [
    #             InlineKeyboardButton(
    #                 text="edit",
    #                 callback_data=f"id{x.message_id}",
    #             )
    #         ],
    #     ]
    # )
    await bot.send_message(chat_id=message.chat.id, text=text)
    # await bot.edit_message_media(
    #     chat_id=message.chat.id,
    #     message_id=message.message_id + 2,
    #     media=InputMediaPhoto(media=media),
    # )
    # await message.answer(

    #     reply_markup=builder.as_markup(resize_keyboard=True),
    # )


# =================================================================
async def application(message: types.Message, key=None):

    contact_button = KeyboardButton(
        text="Отправить свой контакт ☎️", request_contact=True
    )
    contact_admin = KeyboardButton(
        text="Номер мастера ☎️",
    )
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[contact_button, contact_admin]], resize_keyboard=True
    )
    # keyboard.add(contact_button)

    await message.answer(
        "Пожалуйста, поделитесь своим контактом или\nвозмите номер мастера",
        reply_markup=keyboard,
    )
