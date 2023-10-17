from aiogram import executor
from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware  # Импортируем BaseMiddleware
from loader import dp
import middlewares, filters, handlers
from utils.set_bot_commands import set_default_commands

class SubscriptionMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data: dict):
        channel_username = "@FilmPremiere"  # Замените на реальное имя вашего канала

        user_id = message.from_user.id
        user = await message.bot.get_chat_member(channel_username, user_id)
        if user.status not in ("member", "administrator", "creator"):
            await message.answer("Для использования бота, пожалуйста, подпишитесь на наш канал. https://t.me/FilmPrimiere")
            return

async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

if __name__ == '__main__':
    dp.middleware.setup(SubscriptionMiddleware())

    executor.start_polling(dp, on_startup=on_startup)
