import asyncio
import random
from aiogram.types import Message
from aiogram.types import Message
import asyncio
from decouple import config
from delete_chat import delete
from aiogram.utils.chat_action import ChatActionSender
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from decouple import config

from wrapper_bot import TelegramBotWrapper


chat_data = {}

TOKEN = config("TOKEN", cast=str, default="пусто")
bot = TelegramBotWrapper(TOKEN)


async def main_menu(message: Message, callback=None):
    """Главное меню"""

    chat_id = message.chat.id
    uid = message.from_user.id
    await delete(chat_id, chat_data)

    greetings = [
        "<b>Здравствуйте! Вы ищете информацию о стоимости работ, потому что хотите знать, какой результат вы можете получить за свои деньги? Я готов помочь вам в этом и предложить оптимальное решение для вашей задачи.</b>",
        # "Привет! Рад вас видеть! Здесь Вы можете узнать стоимость некоторых работ.",
        # "Здравствуйте! Вы обратились к боту для ознакомления стоимости работ. Укажите, пожалуйста, вид работ, который вас интересует.",
        # "Добрый день! Я здесь, чтобы  показать Вам стоимость некоторых работ.",
        # "Здравствуйте! Нужна информация о стоимости работ? Выберите, какой вид работ вас интересует, и я с удовольствием помогу.",
    ]
    welcome_message = random.choice(greetings)

    print("Пришло в main_menu")
    try:
        builder = ReplyKeyboardBuilder()

        ADMIN = config("ADMIN", cast=lambda x: x.split(","), default="пусто")

        if str(uid) in ADMIN:
            kb = ["👉 Плитка", "👉 Гипсокартон", "📝 Оствить заявку", "⚙️ Информация"]
        else:
            kb = ["👉 Плитка", "👉 Гипсокартон", "📝 Оствить заявку"]
        for text in kb:
            builder.add(types.KeyboardButton(text=text))
        builder.adjust(2, 1)

        if callback is None:
            async with ChatActionSender(
                bot=bot, chat_id=message.from_user.id, action="typing"
            ):
                await asyncio.sleep(1)

            message_menu = await message.answer(
                welcome_message,
                reply_markup=builder.as_markup(resize_keyboard=True),
            )

        return
    except Exception as e:
        print(e, "< --- def main_menu")
    message_menu = await message.answer(
        welcome_message,
        reply_markup=builder.as_markup(resize_keyboard=True),
    )
    chat_data[chat_id] = {"user_messages": [message_menu.message_id]}
