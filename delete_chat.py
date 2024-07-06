from decouple import config
from wrapper_bot import TelegramBotWrapper


TOKEN = config("TOKEN", cast=str, default="пусто")
bot = TelegramBotWrapper(TOKEN)


async def delete(chat_id, chat_data):
    if chat_id in chat_data:
        for message_id in chat_data[chat_id].get("user_messages", []):
            try:
                await bot.delete_message(chat_id, message_id)
            except Exception as e:
                print(f"Не удалось удалить сообщение {message_id}: {e}")


# chat_data[chat_id] = {"user_messages": [welcome_message.message_id]}
