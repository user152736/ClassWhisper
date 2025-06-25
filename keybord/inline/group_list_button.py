from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.database_connection import GroupTable, session

group_list = session.query(GroupTable.name).all()
builder = InlineKeyboardBuilder()
for group in group_list:
    group_name = group[0]
    builder.button(text=group_name, callback_data=f"group_{group_name}")
builder.adjust(1)
