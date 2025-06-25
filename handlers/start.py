
from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from config.config import ADMIN
from keybord.regular.buttons import group_buttons

start_router = Router()

@start_router.message(CommandStart())
async def command_start_handler(message: Message):
    fullname = html.bold(message.from_user.full_name)
    if message.from_user.id == int(ADMIN):
        await message.answer('botga xush kelibsiz Admin', reply_markup=group_buttons())
    else:
        fullname = html.bold(message.from_user.full_name)
        await message.answer(f"Salom, {fullname}!\n\n"
                             f"Bu bot sizga farzandigizni o'zlashtirish ko'rsatkichlari haqida xabar berib boradi!")