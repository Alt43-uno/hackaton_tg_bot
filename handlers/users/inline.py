import random
from random import randint

from aiogram import types, Router, Bot, F
from aiogram.filters import CommandStart

from aiogram.fsm.context import FSMContext

from filters.Filter import ChatFilter
from keyboards.default import main_keyboard
from config import dp, Users
from db.models import User
from keyboards.inline import inline_cancel_kb, inline_back_uniq_kb, inline_get_service_kb


router = Router()
dp.include_router(router)


@router.callback_query(ChatFilter(type="callback"), F.data == "cancel")
async def profile(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text('<b>Отменено</b>')
    await callback.message.delete()
    await callback.answer()
    await state.clear()


@router.callback_query(ChatFilter(type="callback"), F.data.startswith('fillial:'))
async def profile(callback: types.CallbackQuery, state: FSMContext):
    filial = callback.data.split(":")[1]
    await state.update_data(filial=filial)
    await callback.message.edit_text("<b>Выберите по какой причине вы посещаете наш банк:</b>", reply_markup=inline_get_service_kb())
    await callback.answer()

@router.callback_query(ChatFilter(type="callback"), F.data.startswith('service:'))
async def profile(callback: types.CallbackQuery, state: FSMContext):
    service = callback.data.split(":")[1]
    filial = (await state.get_data())['filial']
    number = random.randint(1,100)
    await callback.message.answer(f"<b>Ваш номер в очереди: {number}\n"
                                     f"Филиал: {filial}\n"
                                     f"Услуга: {service}</b>")
    await callback.message.delete()
    await callback.answer()