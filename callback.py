import asyncio
from aiogram import types, Dispatcher, Router
from aiogram.types import Message, BotCommand, InputFile, CallbackQuery
from aiogram.filters import Command

2

from aiogram.enums import content_type
from aiogram import F
from utils import (
    add_user_to_db,
    application,
    gipsokarton_key,
    plitka_key,
    plitka_key_choice_price,
)
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

from menu import main_menu


TOKEN = config("TOKEN", cast=str, default="пусто")
bot = TelegramBotWrapper(TOKEN)
dp = Dispatcher()


async def main():
    # Запуск поллинга
    # await bot.set_my_commands([BotCommand(command="start", description="Начать")])
    await dp.start_polling(bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


chat_data = {}


@dp.message(Command(commands=["start"]))
async def clear_chat_and_send_welcome(message: types.Message):
    print("Start bot")
    chat_id = message.chat.id

    # Очистка предыдущих сообщений
    if chat_id in chat_data:
        for message_id in chat_data[chat_id].get("user_messages", []):
            try:
                await bot.delete_message(chat_id, message_id)
                print("Start bot - 2")
            except Exception as e:
                print(f"Не удалось удалить сообщение {message_id}: {e}")

    # Отправка приветственного сообщения
    welcome_message = await message.answer(
        "Добро пожаловать! Ваше сообщение сохранено."
    )
    print("Start bot - 3")
    # Обновление chat_data с ID нового сообщения
    chat_data[chat_id] = {"user_messages": [welcome_message.message_id]}

    # занести пользователя в базу
    # await add_user_to_db(
    #     user_id=message.from_user.id,
    #     username=message.from_user.username,
    #     first_name=message.from_user.first_name,
    #     last_name=message.from_user.last_name,
    # )

    # вызвать главное меню
    print("await main_menu(message)")
    await main_menu(message)


# =================================================================
@dp.message(F.text.startswith("👉 Ст"))
async def plitka(message: types.Message):
    """Стоимость работ"""

    print("Стоимость работ")
    await plitka_key(message)


@dp.message(F.text.startswith("👉 Ги"))
async def gipsokarton(message: types.Message):
    await gipsokarton_key(message)
    # await message.reply("Гипсокартон!")


@dp.message(F.text.startswith("📝 Ос"))
async def gipsokarton(message: types.Message):
    await application(message)
    # await message.reply("Гипсокартон!")


# =================================================================


@dp.message(F.text.startswith(("Пол", "Стены", "Санузел", "Объём")))
async def plitka(message: types.Message):

    print(message.text)
    if message.text == ("Пол"):
        key = 1

    if message.text == ("Санузел"):
        key = 2
    if message.text == ("Объём"):
        key = 3

    # keyboard = await plitka_key(message)

    # await message.answer(reply_markup=keyboard, text="Выбор работ")
    await plitka_key_choice_price(message, key=key)


# =================================================================


@dp.message(F.text.startswith("Номер"))
async def mail(msg: types.Message):
    await msg.answer(f"Тел. мастера: 8(900)111-11-111")

    mention = (
        f'<a href="tg://user?id=@{msg.from_user.id}">{msg.from_user.first_name}</a>'
    )
    await bot.send_message(
        5744848801, text=f"Запрос контакта от {mention}", parse_mode="HTML"
    )
    # await bot.send_message(5744848801, text=f"{msg.from_user.id}")
    # #
    # await bot.send_message(5744848801, text=f"{msg.chat.first_name}")
    #
    # mention = f"[{msg.from_user.first_name}](tg://user?id={msg.from_user.id})"
    # await bot.send_message(5744848801, f"Привет, {mention}!", parse_mode="HTML")


# =================================================================


@dp.message(F.contact)
async def func_contact(msg: Message):
    await msg.answer(f"Спасибо.В ближайшее время мы Вам позвоним.")
    # await msg.answer(f"Контакт:{msg.contact.phone_number}")
    await bot.send_message(5744848801, text=f"Заказ")
    await bot.send_message(5744848801, text=f"{msg.contact.phone_number}")

    contact = msg.contact
    phone_number = contact.phone_number
    first_name = contact.first_name
    user_id = contact.user_id
    print(phone_number, "\n", user_id, "\n", first_name)


# ----------------------------------------------------------------
