from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! IjaraBotga xush kelibsiz.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)