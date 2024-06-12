from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline import get_final_kb, num_kb
from user import User
from utils.states import question

router = Router()


@router.callback_query(F.data == "start")
async def question_start(query: CallbackQuery, state: FSMContext, bot: Bot) -> None:
    user = User()
    ms = user.next()
    await state.set_state(question.one)
    await state.update_data(user=user)
    await query.message.edit_reply_markup()
    await bot.send_message(query.message.chat.id, ms, reply_markup=num_kb)


@router.callback_query(F.data.isdigit(), question.one)
async def question_reply(query: CallbackQuery, state: FSMContext, bot: Bot) -> None:
    user = await state.get_data()
    user = user["user"]
    user.reply = int(query.data)
    ms = user.next()
    if user.question <= 7:
        await state.update_data(user=user)
        await query.message.edit_text(ms, reply_markup=num_kb)
    else:
        await state.clear()
        await query.message.delete()
        await bot.send_photo(chat_id=query.message.chat.id, caption=ms[0], photo=ms[1], reply_markup=get_final_kb(user))