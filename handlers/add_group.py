from aiogram import Router, F
from aiogram.types import Message
from config.config import ADMIN
from database.database_connection import session, GroupTable
from aiogram.fsm.context import FSMContext
from states.states import AddGroup

add_group_router = Router()


@add_group_router.message(F.text == 'Guruh yaratish 👥')
async def add_group_func(message:Message ,state:FSMContext):
    if message.from_user.id == int(ADMIN):
        await message.answer(text='Guruh nomini kiriting')
        if message.from_user.id == int(ADMIN):
            await state.set_state(AddGroup.group_name)

@add_group_router.message(AddGroup.group_name)
async def group_name_state(message:Message ,state:FSMContext):
    if len(message.text) > 50:
        await message.answer('Guruh nomi 50 ta harfdan yuqori bola olmaydi iltimos qayta urinib ko`ring.')
    group_table = GroupTable(name=message.text)
    group_table.save(session)
    await message.answer('Guruh yaraldi')
    await state.clear()




