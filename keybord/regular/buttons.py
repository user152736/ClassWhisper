from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def group_buttons():
    button = ReplyKeyboardMarkup(
        keyboard=[
            [
                # create group button
                KeyboardButton(text='Guruh yaratish 👥'),

                # group list button
                KeyboardButton(text='Guruhlar ro`yxati 📝')
            ]
        ],
        resize_keyboard=True
    )

    return button

