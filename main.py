import asyncio
from aiogram import Bot
import logging

from aiogram.exceptions import TelegramBadRequest
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat

from config import ADMINS

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s %(asctime)s %(levelname)s %(message)s")


async def on_startup(bot: Bot):
    logger.info('Bot was started')


async def set_commands(bot):
    commands = [BotCommand(command="start", description="🗯 Меню")]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())



async def main():
    from config import bot, dp
    import middlewares
    import handlers
    dp.startup.register(on_startup)
    await set_commands(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
