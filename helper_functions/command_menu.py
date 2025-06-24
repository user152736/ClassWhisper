from aiogram.types import BotCommand
from aiogram import Bot

async def main_menu(bot:Bot):
    main_menu_commands = [
        BotCommand(command='/start', description='start')
    ]

    await bot.set_my_commands(main_menu_commands)