from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from config_reader import ini_config

router = Router()


@router.message(Command("contact"))
async def contact(message: Message) -> None:
    ms = ini_config("text", "contacts", "guardianship")
    await message.answer(ms, reply_markup=None)