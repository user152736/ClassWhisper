from aiogram import Router ,F, html
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from sqlalchemy import select

from states.states import AddStudent

# database
from database.database_connection import StudentsTable, GroupTable ,session

# regex filter
import re


adding_student_router = Router()

@adding_student_router.callback_query(F.data.startswith("add:"))
async def on_add_student(callback: CallbackQuery, state:FSMContext):
    group_name = callback.data.split(":", 1)[1]
    await state.update_data(group_name=group_name)
    await state.set_state(AddStudent.student_name)
    await callback.answer('O`quvchining ismini kirirting')
    await callback.message.answer('O`quvchining ismini kirirting')

@adding_student_router.message(AddStudent.student_name)
async def student_name_state(message:Message, state:FSMContext):
    if len(message.text) <= 50:
        await state.update_data(student_name=message.text)
        await state.set_state(AddStudent.parents_name)
        await message.answer('O`quvchining ota onasini ismini kirting')
    else:
        await message.answer('O`quvchining ismi 50 ta harfdan ko`p bo`lishi mumkin emas\n'
                             'iltimos qayta urining')

@adding_student_router.message(AddStudent.parents_name)
async def parents_name_state(message:Message, state:FSMContext):
    itl = html.italic
    if len(message.text) <= 50:
        await state.update_data(parents_name=message.text)
        await state.set_state(AddStudent.parents_phone_number)
        await message.answer('O`quvchining ota onasinining telefon raqamini kirirting\n'
                             f'telefon raqam formati {itl('+998*********')}')
    else:
        await message.answer('O`quvchi ota onasining ismi 50 ta harfdan ko`p bo`lishi mumkin emas\n'
                             'iltimos qayta urining')

@adding_student_router.message(AddStudent.parents_phone_number)
async def phone_number_state(message:Message, state:FSMContext):
    itl = html.italic
    phone_number = message.text
    pattern = r'^\+998(90|91|93|94|97|98|99|95|55|88|77|33)\d{7}$'
    if not re.match(pattern,phone_number):
        return await message.answer('iltimos telefon raqamni keltirilgan misol bo`yicha kirirting'
                                    f'telefon raqam formati {itl('+998*********')}')
    await state.update_data(phone_number=phone_number)

    data = await state.get_data()
    group = session.query(GroupTable).filter_by(name=data['group_name']).first()

    student = StudentsTable(student_name=data['student_name'],
                            parents_name=data['parents_name'],
                            parents_phone_number=data['phone_number'],
                            group_name_id=group.id)
    await message.answer('O`quvchi ro`yxatga qo`shildi')
    student.save(session)
    await state.clear()













