from aiogram import Router, F
from aiogram.types import Message
from config.config import ADMIN
from keybord.inline.group_list_button import builder

group_list_router = Router()





@group_list_router.message(F.text == 'Guruhlar ro`yxati 📝')
async def list_group_func(message:Message):

    if message.from_user.id == int(ADMIN):
        await message.answer(
                        f'Mavjud guruhlar royxati',
                        reply_markup=builder.as_markup()
                             )

