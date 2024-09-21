import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, input_file
from wiki import wiki
from cat import cat_img

dp = Dispatcher()

TOKEN = "7015438221:AAGQYE-XxJwfNnOr_2fxGPctceAPLvhHDYQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Bu bizning birinchi botimiz"
    await message.answer(text)

@dp.message(Command("cat"))
async def cat(message: Message):
    image = cat_img()
    if image:
        await message.answer_document(document=input_file.BufferedInputFile(file=image, filename="cat.png"))

@dp.message(F.text)
async def wiki_handler(message: Message):
    text = message.text

    malumot = wiki(text)
    await message.answer(malumot)
    # await message.reply(malumot)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
