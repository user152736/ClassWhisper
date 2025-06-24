
from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

start_router = Router()

@start_router.message(CommandStart())
async def command_start_handler(message: Message):
    fullname = html.bold(message.from_user.full_name)
    await message.answer(f"Salom, {fullname}!\n\n Bu bot sizga farzandigizni o'zlashtirish ko'rsatkichlari haqida xabar berib turadi!")