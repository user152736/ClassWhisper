from aiogram.fsm.state import State, StatesGroup

class AddGroup(StatesGroup):
    group_name = State()

class AddStudent(StatesGroup):
    student_name = State()
    parents_name = State()
    parent_user_id = State()