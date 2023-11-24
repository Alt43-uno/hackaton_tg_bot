from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


back_button = InlineKeyboardButton(text="◀️ Назад", callback_data="back")
cancel_button = InlineKeyboardButton(text="↩️ Отмена", callback_data="cancel")


def inline_cancel_kb():
    builder = InlineKeyboardBuilder()
    builder.add(cancel_button)
    builder.adjust(1)
    return builder.as_markup()


def inline_back_kb():
    builder = InlineKeyboardBuilder()
    builder.add(back_button)
    builder.adjust(1)
    return builder.as_markup()

def inline_get_filials_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="ул. Юнусалиева 74/2",
        callback_data=f"fillial:{1}")
    )
    builder.add(InlineKeyboardButton(
        text="ул. Московская 205",
        callback_data=f"fillial:{2}")
    )
    builder.add(InlineKeyboardButton(
        text="ул. Валерия 221",
        callback_data=f"fillial:{3}")
    )
    builder.adjust(2)
    builder.row(cancel_button)
    return builder.as_markup()

def inline_get_service_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Кредитование",
        callback_data=f"service:{1}")
    )
    builder.add(InlineKeyboardButton(
        text="Банковские карты",
        callback_data=f"service:{2}")
    )
    builder.add(InlineKeyboardButton(
        text="Юр. лицам",
        callback_data=f"service:{3}")
    )
    builder.add(InlineKeyboardButton(
        text="Физ. лицам",
        callback_data=f"service:{4}")
    )
    builder.adjust(2)
    builder.row(cancel_button)
    return builder.as_markup()

def inline_back_uniq_kb(reply):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="◀️ Назад", callback_data=reply))
    builder.adjust(1)
    return builder.as_markup()

