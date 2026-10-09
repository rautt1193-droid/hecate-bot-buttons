import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from dotenv import load_dotenv
from aiohttp import web
import asyncio

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

async def handle(request):
    return web.Response(text="Bot is running!")

async def main():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.environ.get('PORT', 8080)))
    await site.start()
    asyncio.create_task(dp.start_polling(bot))
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
