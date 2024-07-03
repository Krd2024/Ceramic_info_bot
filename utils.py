from wrapper_bot import TelegramBotWrapper
import asyncio
from aiogram import types, Dispatcher, Router

# from aiogram.types import Message, BotCommand, InputFile, CallbackQuery
# from aiogram.filters import Command
# from aiogram import F
from aiogram.types import (
    Message,
    InputMediaPhoto,
    InputMedia,
    ContentType,
    InputMediaAnimation,
)

from decouple import config

from aiogram import types

from decouple import config

# from aiogram.types import FSInputFile, URLInputFile

from aiogram.methods.edit_message_media import EditMessageMedia
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import aiosqlite
from aiogram.types import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from aiogram import types
from img import *
from delete_chat import delete


TOKEN = config("TOKEN", cast=str, default="пусто")
bot = TelegramBotWrapper(TOKEN)


# Функция для добавления пользователя в базу данных
# Асинхронная функция для добавления пользователя в базу данных
# async def add_user_to_db(user_id, username, first_name, last_name):
#     # Устанавливаем соединение с базой данных SQLite
#     async with aiosqlite.connect("sqlite.db") as conn:
#         # Создаем курсор для выполнения SQL-запросов
#         async with conn.cursor() as cursor:
#             # Выполняем запрос на вставку данных пользователя
#             await cursor.execute(
#                 """
#                 INSERT INTO users (user_id, username, first_name, last_name)
#                 VALUES (?, ?, ?, ?)
#                 """,
#                 (user_id, username, first_name, last_name),
#             )
#             # Коммитим изменения в базу данных
#             await conn.commit()


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
        "Санузел",
        "Объём",
        "📝 Оставить заявку",
        "⬅️ Назад",
    ]
    # for i in range(1, 5):
    for i in list_products:
        builder.add(types.KeyboardButton(text=str(i)))
    builder.adjust(3, 1, 1)
    # reply_markup = builder.as_markup(resize_keyboard=True)
    # return reply_markup
    await message.answer(
        "Выберите:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )


chat_data = {}


async def plitka_key_choice_price(message: types.Message, key=None):

    chat_id = message.chat.id
    print(key)
    # Очистка предыдущих сообщений
    await delete(chat_id, chat_data)

    # =================================================================
    if key == 1:
        caption = f"Создание каркаса для объёмных конструкций ...\nЦена от 1800 руб\n"
        media = plitka_pol

    elif key == 2:
        caption = f"Выравнивание стен...\nЦена от 1800 руб\n"
        media = plitka_sanuzel

    elif key == 3:
        caption = f"Возведение перегородок...\nЦена от 1300 руб\n"
        media = plitka_many
    elif key == 3:
        caption = f"Отделка потолков...\nЦена от 1300 руб\n"
        media = plitka_many

    builder = ReplyKeyboardBuilder()

    # list_products = ["⬅️ Назад", "📝 Оставить заявку или уточнить детали"]
    # # for i in range(1, 5):
    # for i in list_products:
    #     builder.add(types.KeyboardButton(text=str(i)))

    # =================================================================
    print(message.chat.id)
    print(message.message_id)

    message_price = await bot.send_photo(message.chat.id, photo=media, caption=caption)
    chat_data[chat_id] = {"user_messages": [message_price.message_id]}
    # await bot.send_message(chat_id=message.chat.id, text=text)


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


# ===================================================================================


async def gipsokarton_key_choice_price(message: types.Message, key=None):

    chat_id = message.chat.id
    print(key)
    # Очистка предыдущих сообщений
    await delete(chat_id, chat_data)

    # =================================================================
    if key == 1:
        caption = f"Укладка  пол...\nЦена от 1800 руб\n"
        media = plitka_pol

    elif key == 2:
        caption = f"Укладка  санузел...\nЦена от 1800 руб\n"
        media = plitka_sanuzel

    elif key == 3:
        caption = f"Укладка  объём...\nЦена от 1300 руб\n"
        media = plitka_many

    builder = ReplyKeyboardBuilder()

    # =================================================================
    print(message.chat.id)
    print(message.message_id)

    message_price = await bot.send_photo(message.chat.id, photo=media, caption=caption)
    chat_data[chat_id] = {"user_messages": [message_price.message_id]}
