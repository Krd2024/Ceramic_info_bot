from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties


class TelegramBotWrapper:
    _instance = None

    def __new__(cls, token):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance = Bot(
                token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
            )
        return cls._instance

    def __getattr__(self, name):
        return getattr(self._instance, name)
