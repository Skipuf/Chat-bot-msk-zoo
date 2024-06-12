from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from config_reader import ini_config
from keyboards.inline import start_kb

router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer_photo(caption=ini_config("text", "start", "text"), photo=ini_config("text", "start", "photo"), reply_markup=start_kb)


@router.message(Command("help"))
async def contact(message: Message) -> None:
    ms = ini_config("text", "help", "text")
    await message.answer(ms)
