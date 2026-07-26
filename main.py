import os
import asyncio
import logging

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.register import router as register_router

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

# ثبت Router
dp.include_router(register_router)


async def main():
    print("Bot Started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())