from pprint import pprint
from typing import Union

from aiogram.filters import Filter
from aiogram.types import Message, CallbackQuery

from config import ADMINS, CHAT_SUPPORT


class AdminFilter(Filter):
    def __init__(self):
        pass

    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.from_user.id in ADMINS


class ChatFilter(Filter):
    def __init__(self, type: str):
        self.type = type

    async def __call__(self, callback: CallbackQuery) -> bool:
        if self.type == "callback":
            return callback.message.chat.id > 0
        else:
            return callback.chat.id > 0


class SupportChatFilter(Filter):
    def __init__(self, type):
        self.type = type

    async def __call__(self, callback: CallbackQuery) -> bool:
        if self.type == "callback":
            return callback.message.chat.id == CHAT_SUPPORT
        else:
            return callback.chat.id == CHAT_SUPPORT
