from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config_reader import ini_config
from user import User

start_kb = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Начать", callback_data="start")
    ]
    ]
)

num_kb = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="1", callback_data="1"),
        InlineKeyboardButton(text="2", callback_data="2"),
        InlineKeyboardButton(text="3", callback_data="3"),
        InlineKeyboardButton(text="4", callback_data="4")
    ]
    ]
)

assess_kb = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="1", callback_data="assess_1"),
        InlineKeyboardButton(text="2", callback_data="assess_2"),
        InlineKeyboardButton(text="3", callback_data="assess_3"),
        InlineKeyboardButton(text="4", callback_data="assess_4"),
        InlineKeyboardButton(text="5", callback_data="assess_5")
    ], [
        InlineKeyboardButton(text="6", callback_data="assess_6"),
        InlineKeyboardButton(text="7", callback_data="assess_7"),
        InlineKeyboardButton(text="8", callback_data="assess_8"),
        InlineKeyboardButton(text="9", callback_data="assess_9"),
        InlineKeyboardButton(text="10", callback_data="assess_10")
    ]
    ]
)


def get_final_kb(_user: User) -> InlineKeyboardMarkup:
    ms = ini_config("text", "question", "final_kb").replace("animal", _user.animal)
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[
                InlineKeyboardButton(text="Узнать больше!", callback_data="guardianship"),
            ], [
                InlineKeyboardButton(text="Поделиться!", switch_inline_query=ms)
            ], [
                InlineKeyboardButton(text="Оценить!", callback_data="assess")
            ], [
                InlineKeyboardButton(text="Попробовать ещё раз?", callback_data="start")
            ]
        ]
    )
    return kb
