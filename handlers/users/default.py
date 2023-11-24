import json

from aiogram import types, Router, Bot, F
from aiogram.filters import CommandStart

from filters.Filter import ChatFilter
from keyboards.default import main_keyboard
from config import dp
from db.models import User
from keyboards.inline import inline_back_uniq_kb, inline_get_filials_kb, inline_get_service_kb

router = Router()
dp.include_router(router)


@router.message(ChatFilter(type="message"), F.text == '🏷 Получить номер в очереди')
async def main_menu(message: types.Message, bot: Bot, user: User):
    await message.answer("<b>Для получения номера в очереди, выберите филиал который вы хотите посетить:</b>", reply_markup=inline_get_filials_kb())
