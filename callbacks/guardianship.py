from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from config_reader import ini_config

router = Router()


@router.callback_query(F.data == "guardianship")
async def guardianship(query: CallbackQuery, bot: Bot) -> None:
    ms = ini_config("text", "guardianship", "text")
    ms += f'\n\n{ini_config("text", "contacts", "guardianship")}'
    ph = ini_config("text", "guardianship", "photo")
    await bot.send_photo(chat_id=query.message.chat.id, caption=ms, photo=ph, reply_markup=None)

