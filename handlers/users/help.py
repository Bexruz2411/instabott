from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("По сотрудничеству: @yusufbekovv24",
            "Наши другие проекты: @Cinema_Magicbot",
            "Наш канал про кино: @FilmPrimiere")
    
    await message.answer("\n".join(text))
