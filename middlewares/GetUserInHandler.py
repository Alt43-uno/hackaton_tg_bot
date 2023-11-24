from pprint import pprint

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject
from typing import Dict, Awaitable, Callable, Any

from config import Users, dp, bot
from db.models import User
from states.user import UserStates


class GetUserInHandler(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]) -> Any:

        username = 'no'

        if event.inline_query:
            user_id = event.inline_query.message.from_user.id
            try:
                username = event.inline_query.message.from_user.username
            except:
                pass
        elif event.message:
            user_id = event.message.from_user.id
            try:
                username = event.message.from_user.username
            except:
                pass
        else:
            return await handler(event, data)
        user = await Users.get_user(user_id)
        if not user:
            if username == 'no':
                await Users.create_user(user_id=user_id, username='None', name=event.message.from_user.first_name, surname=event.message.from_user.last_name)
            else:
                await Users.create_user(user_id=user_id, username=username, name=event.message.from_user.first_name, surname=event.message.from_user.last_name)
            user = await Users.get_user(user_id)
        data['user'] = user
        return await handler(event, data)


dp.update.middleware.register(GetUserInHandler())
