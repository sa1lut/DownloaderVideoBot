import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config.config import settings
from handlers import commands

# Включим логирование для отслеживания ошибок
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def register_routers(dp: Dispatcher):
    dp.include_router(commands.router)

async def main():
    bot = Bot(token=settings.bot_token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()

    register_routers(dp)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())