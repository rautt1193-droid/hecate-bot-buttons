import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# Ссылки (замените на свои реальные ссылки)
BIBLIOTEKA_URL = "https://max.ru/join/vTjoOxMHso6R8o_fkAMK0Hy0xZKJzQDjLXqjOUevit8"
OTZYVY_URL = "https://max.ru/join/QbOcU2j9OIzQeEK9-dlg2QVwBZhFTD_KreiUM6r2Kx0"
WEBAPP_URL = "https://rautt1193-droid.github.io/hecate-store/"

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌙 Открыть магазин", web_app=WebAppInfo(url=WEBAPP_URL))],
        [InlineKeyboardButton(text="📚 Библиотека знаний", url=BIBLIOTEKA_URL)],
        [InlineKeyboardButton(text="⭐ Отзывы", url=OTZYVY_URL)],
    ])
    await message.answer(
        "🌙 Добро пожаловать в мастерскую «Дары Гекаты»!\n\n"
        "Наши изделия изготовлены с любовью и вниманием к каждой детали, "
        "заряжены энергией древних традиций и обладают особой силой.\n\n"
        "Выберите действие:",
        reply_markup=keyboard
    )

@dp.message(Command("menu"))
async def cmd_menu(message: types.Message):
    await cmd_start(message)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
