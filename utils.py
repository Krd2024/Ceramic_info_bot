import sqlite3
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
from aiogram.types import FSInputFile
from text import text_plitka, text_gips


TOKEN = config("TOKEN", cast=str, default="пусто")
bot = TelegramBotWrapper(TOKEN)

chat_data = {}


async def add_user_to_db(user_id, username, first_name):
    async with aiosqlite.connect("db.sqlite3") as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(
                """
                INSERT INTO users (user_id, username, first_name)
                VALUES (?, ?, ?)
                """,
                (user_id, username, first_name),
            )

            await conn.commit()


# =================================================================
# chat_data = {}


async def admin_info_db(message):
    chat_id = message.chat.id

    await delete(chat_id, chat_data)

    with sqlite3.connect("db.sqlite3") as connection:
        cursor = connection.cursor()
        cursor.execute(
            """SELECT username, user_id,first_name,timestamp as time FROM users"""
        )
        res = cursor.fetchall()
        info = ""
        for row in res:
            info += f"\nИмя:{row[2]}\nUsername:{row[0]}\nId:{row[1]}\nВремя:{row[3]}\n*"

        # print(info)

        ADMIN = config("ADMIN", cast=lambda x: x.split(","), default="пусто")

        for admin_id in ADMIN:
            # print(admin_id)
            if info == "":
                info = f"Нет сообщений"

            message_info = await bot.send_message(admin_id, info)
            chat_data[chat_id] = {"user_messages": [message_info.message_id]}
        # import asyncio

        # tasks = [bot.send_message(admin_id, info) for admin_id in ADMIN]
        # await asyncio.gather(*tasks)


# =================================================================


async def gipsokarton_key(message: types.Message):
    builder = ReplyKeyboardBuilder()
    list_products = [
        "Создание каркаса для объёмных конструкций",
        "Выравнивание стен ",
        "Возведение перегородок",
        "Отделка потолков",
        "⬅️ Назад",
        "📝 Оставить заявку",
    ]
    # for i in range(1, 5):
    for i in list_products:
        builder.add(
            types.KeyboardButton(text=str(i), parse_mode="HTML", color=(0, 0, 255))
        )
    builder.adjust(1, 3, 2)

    await message.answer(
        text=text_gips,
        reply_markup=builder.as_markup(
            resize_keyboard=True, input_field_placeholder="Воспользуйтесь меню:"
        ),
    )


# =================================================================


async def plitka_key(message: types.Message):
    uid = message.from_user.id
    builder = ReplyKeyboardBuilder()
    list_products = [
        "Пол",
        "Санузел",
        "Объём",
        "⬅️ Назад",
        "📝 Оставить заявку",
    ]
    # for i in range(1, 5):
    for i in list_products:
        builder.add(types.KeyboardButton(text=str(i)))
    builder.adjust(3, 2)

    await message.answer(
        text=text_plitka,
        reply_markup=builder.as_markup(
            resize_keyboard=True, input_field_placeholder="Воспользуйтесь меню:"
        ),
    )


# =================================================================

# chat_data = {}


async def plitka_key_choice_price(message: types.Message, key=None):

    uid = message.from_user.id
    chat_id = message.chat.id

    # Очистка предыдущих сообщений
    await delete(chat_id, chat_data)

    # =================================================================
    if key == 1:
        caption = f"Пол ...\nЦена от 1800 руб\n"
        message_price = await message.answer_animation(gif_pol, caption=caption)
        chat_data[chat_id] = {"user_messages": [message_price.message_id]}
        return

    elif key == 2:
        caption = f"Санузел...\nЦена от 1800 руб\n"
        media = plitka_sanuzel

    elif key == 3:
        caption = f"Объём...\nЦена от 1300 руб\n"
        media = plitka_many

    elif key == 4:
        await delete(chat_id, chat_data)
        await main_menu(message)
        return

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
    contact_back = KeyboardButton(
        text="⬅️ Назад",
    )
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[contact_button, contact_admin], [contact_back]], resize_keyboard=True
    )

    await message.answer(
        "Пожалуйста, поделитесь своим контактом или\nвозмите номер мастера",
        reply_markup=keyboard,
    )

    # ===================================================================================

    "⏱️🫗🫵👉⚙️0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟▪️☑️🫵👍🔘📝⏳🟢🔶✔️❌⚠️✅☑️"
    "🔘₽¹⁴₁⑶⒈⒉⒌⒍⒎⒏⒐⒑⒒⒓⒔⒕⒖⒗⒘"


async def gipsokarton_key_choice_price(message: types.Message, key=None):

    chat_id = message.chat.id

    # Очистка предыдущих сообщений
    await delete(chat_id, chat_data)
    # =================================================================
    if key == 1:
        caption = f"👉 Каркас может быть использован для создания различных конструкций, таких как:\n✅ Стены\n✅ Потолки\n✅ Перегородки\n✅ Ниши\n✅ Полки и декоративные элементы\nЦена от ... руб"
        media = gips_ob

    elif key == 2:
        caption = f"""👉 Быстрый и экономичный способ создания ровных стен с идеальной поверхностью.\nПлюсы:\n✅ Быстрота монтажа\n✅ Возможность скрыть коммуникации и дефекты стены\n✅ Идеальная поверхность для финишной отделки\nЦена от ... руб\n"""
        media = viravnivanie_sten_gips

        # media = viravnivanie_sten_gips

    elif key == 3:
        caption = f"👉 Плюсы:\n✅ Быстрота монтажа\n✅ Идеальная поверхность для финишной отделки\nЦена от ... руб\n"

        media = peregorodka_gips
    elif key == 4:
        caption = f"👉 Отделка потолков...\nЦена от ... руб\n"
        media = potolok_gips

    # =================================================================
    # print(message.chat.id)
    # print(message.message_id)

    message_price = await bot.send_photo(message.chat.id, photo=media, caption=caption)
    chat_data[chat_id] = {"user_messages": [message_price.message_id]}
