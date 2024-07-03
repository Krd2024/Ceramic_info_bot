import asyncio
import random
from aiogram import types, Dispatcher, Router
from aiogram.types import Message, BotCommand, InputFile, CallbackQuery
from aiogram.filters import Command
from aiogram import F

# from utils import add_user_to_db
from aiogram.types import (
    Message,
    InputMediaPhoto,
    InputMedia,
    ContentType,
    InputMediaAnimation,
)

from decouple import config
from delete_chat import delete
from wrapper_bot import TelegramBotWrapper

from aiogram import Dispatcher, types

# from aiogram import MemoryStorage
from decouple import config
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.types import FSInputFile, URLInputFile

from aiogram.methods.edit_message_media import EditMessageMedia

from aiogram.utils.keyboard import ReplyKeyboardBuilder

chat_data = {}


async def main_menu(message: Message, callback=None):
    """Главное меню"""

    chat_id = message.chat.id
    await delete(chat_id, chat_data)

    greetings = [
        "Добро пожаловать! Я помогу Вам узнать стоимость некоторых работ?",
        "Привет! Рад вас видеть! Здесь Вы можете узнать стоимость некоторых работ.",
        "Здравствуйте! Вы обратились к боту для ознакомления стоимости работ. Укажите, пожалуйста, вид работ, который вас интересует.",
        "Добрый день! Я здесь, чтобы  показать Вам стоимость некоторых работ.",
        "Здравствуйте! Нужна информация о стоимости работ? Выберите, какой вид работ вас интересует, и я с удовольствием помогу.",
    ]
    welcome_message = random.choice(greetings)

    print("Пришло в main_menu")
    try:
        builder = ReplyKeyboardBuilder()

        kb = [
            "👉 Плитка",
            "👉 Гипсокартон",
            "📝 Оствить заявку",
        ]
        for text in kb:
            builder.add(types.KeyboardButton(text=text))
        builder.adjust(2, 1)

        if callback is None:
            message_menu = await message.answer(
                welcome_message,
                reply_markup=builder.as_markup(resize_keyboard=True),
            )

        chat_data[chat_id] = {"user_messages": [message_menu.message_id]}

        return
    except Exception as e:
        print(e, "< --- def main_menu")

        # keyboard = types.ReplyKeyboardMarkup(
        #     keyboard=kb,
        #     resize_keyboard=True,
        #     # one_time_keyboard=True,
        #     input_field_placeholder="Выберите вид работ",
        # )
        # keyboard.adjust(2)
        # kb = [
        #     types.KeyboardButton(text="👉 Стоимость работ по укладки плитки* "),
        #     types.KeyboardButton(text="👉 Гипсокартон"),
        #     types.KeyboardButton(text=f"📝 Оствить заявку"),
        # ]
