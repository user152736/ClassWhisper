from aiogram import Router ,F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from states.states import AddStudent


adding_student_router = Router()

@adding_student_router.callback_query(F.data.startswith("add:"))
async def on_add_student(callback: CallbackQuery, message:Message, state:FSMContext):
    group_name = callback.data.split(":", 1)[1]
    await state.update_data(group_name=group_name)
    await state.set_state(AddStudent.student_name)
    await message.answer('O`quvchining ismini kirirting')

@adding_student_router.message(AddStudent.student_name)
async def student_name_state(message:Message, state:FSMContext):
    if len(message.text) >= 50:
        await state.update_data(student_name=message.text)
        await state.set_state(AddStudent.parents_name)
        await message.answer('O`quvchining ota onasini ismini kirting')
    else:
        await message.answer('O`quvchining ismi 50 ta harfdan ko`p bo`lishi mumkin emas\n'
                             'iltimos qayta urining')













