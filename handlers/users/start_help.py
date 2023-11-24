from aiogram import types, Router, Bot
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from filters.Filter import ChatFilter
from keyboards.default import main_keyboard
from config import dp, Users
from db.models import User

router = Router()
dp.include_router(router)


@router.message(ChatFilter(type="message"), CommandStart(), StateFilter("*"))
async def start(message: types.Message, bot: Bot, user: User, state: FSMContext):
    await state.clear()
    if message.chat.id > 0:
        user = (await Users.get_user(user_id=message.from_user.id))
        if user:
            await message.answer('Добро пожаловать в EBVR Bank!\n'
                                 'Выберите вариант из меню:', reply_markup=main_keyboard())
    else:
        await message.answer(text="Я запускаюсь только в личном чате", reply_markup=ReplyKeyboardRemove())
