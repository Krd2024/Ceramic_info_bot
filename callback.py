from aiogram import types, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
from utils import (
    add_user_to_db,
    admin_info_db,
    application,
    gipsokarton_key,
    gipsokarton_key_choice_price,
    plitka_key,
    plitka_key_choice_price,
)
from aiogram.types import Message
from decouple import config
from aiogram.types import FSInputFile
from aiogram.methods.edit_message_media import EditMessageMedia
from aiogram import Dispatcher, types

from wrapper_bot import TelegramBotWrapper
from menu import main_menu


TOKEN = config("TOKEN", cast=str, default="пусто")
bot = TelegramBotWrapper(TOKEN)
dp = Dispatcher()


# async def set_commands():
#     commands = [
#         BotCommand(command="start", description="Старт"),
#         # BotCommand(command="start_2", description="Старт 2"),
#         # BotCommand(command="start_3", description="Старт 3"),
#     ]
#     await bot.set_my_commands(commands, BotCommandScopeDefault())


async def main():
    # Запуск поллинга
    # await bot.set_my_commands([BotCommand(command="start", description="Начать")])
    await dp.start_polling(bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
    # await set_commands()


from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.utils.media_group import MediaGroupBuilder

chat_data = {}

from img import *


@dp.message(Command(commands=["start"]))
async def clear_chat_and_send_welcome(message: types.Message):
    print("Start bot")
    uid = message.from_user.id

    # =================================================================
    # занести пользователя в базу
    ADMIN = config("ADMIN", cast=lambda x: x.split(","), default="пусто")
    if str(uid) not in ADMIN:
        await add_user_to_db(
            user_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
        )

    # ===============================================================
    #    ----------------- Альбом -----------

    # album_builder = MediaGroupBuilder(caption="Общая подпись для будущего альбома")

    # album_builder.add_photo(media=plitka_sanuzel)
    # album_builder.add_photo(media=plitka_many)
    # album_builder.add_photo(media=peregorodka_gips)
    # await message.answer_media_group(
    #     # Не забудьте вызвать build()
    #     media=album_builder.build()
    # )
    # ----------------------------------------------------------------
    # Отправка файла из файловой системы
    # file_ids = []

    # image_from_pc = FSInputFile("viravnivanie_sten.jpg")
    # result = await message.answer_photo(
    #     image_from_pc, caption="Изображение из файла на компьютере"
    # )
    # #  для фото

    # file_ids.append(result.photo[0].file_id)
    # print(file_ids)

    # image_from_pc = FSInputFile("peregorodka.jpeg")
    # result = await message.answer_photo(
    #     image_from_pc, caption="Изображение из файла на компьютере"
    # )
    # #  для фото
    # file_ids.append(result.photo[0].file_id)
    # print(file_ids)

    # image_from_pc = FSInputFile("potolok.jpg")
    # result = await message.answer_photo(
    #     image_from_pc, caption="Изображение из файла на компьютере"
    # )
    # #  для фото
    # file_ids.append(result.photo[0].file_id)
    # print(file_ids)

    # image_from_pc = FSInputFile("stena.gif")
    # result = await message.answer_animation(
    #     image_from_pc, caption="Изображение из файла на компьютере"
    # )
    # file_id = result.video.file_id
    # file_ids.append(file_id)
    # # print(result)
    # print(f"File ID: {file_id}")
    # --------------------------------

    # для гиф
    # file_id = result.animation.file_id
    # file_ids.append(file_id)
    # print(f"File ID: {file_id}")

    # ================================================================

    # h = "soobshenie @maxkalinin"
    # await bot.send_message(message.from_user.id, h)

    # вызвать главное меню

    print("await main_menu(message)")
    await main_menu(message)


# =================================================================
@dp.message(F.text.startswith("👉 Пл"))
async def plitka(message: types.Message):
    """Стоимость работ"""

    await plitka_key(message)


@dp.message(F.text.startswith("👉 Ги"))
async def gipsokarton(message: types.Message):
    await gipsokarton_key(message)
    # await message.reply("Гипсокартон!")


@dp.message(F.text.startswith("📝 Ос"))
async def tel(message: types.Message):
    await application(message)


@dp.message(F.text.startswith("⚙️ Инфо"))
async def info(message: types.Message):
    await admin_info_db(message)
    # await message.reply("Гипсокартон!")


# =================================================================


@dp.message(F.text.startswith(("Пол", "Стены", "Санузел", "Объём", "⬅️ Назад")))
async def plitka(message: types.Message):
    chat_id = message.chat.id

    print(message.text)
    if message.text == ("Пол"):
        key = 1

    elif message.text == ("Санузел"):
        key = 2
    elif message.text == ("Объём"):
        key = 3
    elif message.text == ("⬅️ Назад"):
        key = 4

    await plitka_key_choice_price(message, key=key)


@dp.message(
    F.text.startswith(("Создание ", "Выравнивание", "Возведение", "Отделка", "⬅️ Назад"))
)
async def plitka(message: types.Message):

    print(message.text)
    if message.text.startswith("Создание "):
        key = 1

    elif message.text.startswith("Выравнивание"):
        key = 2
    elif message.text.startswith("Возведение"):
        key = 3
    elif message.text.startswith("Отделка"):
        key = 4
    elif message.text == ("⬅️ Назад"):
        await main_menu(message)
        return

    # elif message.text == ("⬅️ Назад"):
    #     await main_menu(message)
    #     return

    # keyboard = await plitka_key(message)
    # await message.answer(reply_markup=keyboard, text="Выбор работ")
    await gipsokarton_key_choice_price(message, key=key)


# =================================================================


@dp.message(F.text.startswith("Номер"))
async def mail(msg: types.Message):
    TELEPHON = config("TELEPHON", cast=str, default="пусто")
    await msg.answer(TELEPHON)
    # await msg.answer(f"Тел. мастера: 8(900)111-11-111")

    # mention = (
    #     f'<a href="tg://user?id={msg.from_user.id}">{msg.from_user.first_name}</a>'
    # )
    # h = f'soobshenie <a href="http://t.me/{message.from_user.username}">max</a>'

    mention = (
        f'<a href="http://t.me/{msg.from_user.username}">{msg.from_user.first_name}</a>'
    )
    await bot.send_message(
        5744848801,
        text=f"Запрос контакта от {mention}\nuser_id {msg.from_user.id}",
        parse_mode="HTML",
    )


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
    mention = (
        f'<a href="http://t.me/{msg.from_user.username}">{msg.from_user.first_name}</a>'
    )
    await bot.send_message(
        5744848801,
        text=f"Запрос контакта от {mention}\nuser_id {msg.from_user.id}",
        parse_mode="HTML",
    )


# ----------------------------------------------------------------
