from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from .group_list import list_group_func


callback_router = Router()

@callback_router.callback_query(F.data.startswith("group_"))
async def handle_group_button(callback: CallbackQuery):
    group_name = callback.data.removeprefix("group_")

    builder = InlineKeyboardBuilder()
    builder.button(text="➕ O`quvchi qoshish", callback_data=f"add:{group_name}")
    builder.button(text="❌ Guruhni o`chirish", callback_data=f"delete:{group_name}")
    builder.button(text="➖ O`quvchini o`chirish", callback_data=f"delete:{group_name}")
    builder.button(text="🔙 Orqaga", callback_data="back:groups")

    builder.adjust(1)

    await callback.message.edit_text(
        f"Вы выбрали группу: {group_name}\nЧто вы хотите сделать?",
        reply_markup=builder.as_markup()
    )
    await callback.answer()





@callback_router.callback_query(F.data.startswith("group:"))
async def on_group_selected(callback: CallbackQuery):
    group_name = callback.data.split(":", 1)[1]
    await callback.message.answer(text='you pressed add student button')

@callback_router.callback_query(F.data == "back:groups")
async def on_back_to_groups(callback: CallbackQuery):
    await list_group_func(callback)







@callback_router.callback_query(F.data.startswith("delete:"))
async def on_delete_group(callback: CallbackQuery):
    group_name = callback.data.split(":", 1)[1]
    await callback.answer(f"Удалить группу {group_name}")




