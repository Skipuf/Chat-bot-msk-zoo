from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from keyboards.inline import assess_kb
from config_reader import ini_config

router = Router()


@router.callback_query(F.data == "assess")
async def assess(query: CallbackQuery, bot: Bot) -> None:
    ms = ini_config("text", "assess", "assess")
    await bot.send_message(chat_id=query.message.chat.id, text=ms, reply_markup=assess_kb)


@router.callback_query(lambda x: x.data[7:].isdigit())
async def assess_final(query: CallbackQuery) -> None:
    ms = ini_config("text", "assess", "final").replace("assess", query.data[7:])
    await query.message.edit_text(text=ms)
