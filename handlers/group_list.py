from aiogram import Router, F
from aiogram.types import Message
from config.config import ADMIN

group_list_router = Router()

@group_list_router.message(F.text == 'Guruhlar ro`yxati 📝')
async def list_group_func(message:Message):
    if message.from_user.id == ADMIN:
        pass
