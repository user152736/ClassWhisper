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


def share_contact():
    button = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Telefon raqam yuborish', request_contact=True)]
        ],
        resize_keyboard=True,
    )

