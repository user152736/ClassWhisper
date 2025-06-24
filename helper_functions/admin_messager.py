from aiogram import Bot, html
from config.config import ADMIN

async def start_up(bot:Bot):
    itl = html.italic
    await bot.send_message(ADMIN, f'{itl('bot ishga tushdi')}')

async def shutdown(bot:Bot):
    itl = html.italic
    await bot.send_message(ADMIN, f'{itl('bot ishlamayapti')}')

