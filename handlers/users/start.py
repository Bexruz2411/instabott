from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from instadownloader import insta
from loader import dp
from aiogram.dispatcher.filters import Text

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}!\n"
                         f"Отправьте ссылку на видео или фото в Instagram. https://t.me/FilmPrimiere
")
@dp.message_handler(Text(startswith='https://www.instagram.com'))
async def test(message: types.Message):
    url = message.text
    wait_message = await message.answer("Подождите ваш контент скачивается...")
    
    result = insta(url)
    if result['type'] == 'error':
        await wait_message.edit_text("К сожалению, по этой ссылке не найдено никакой информации!")
    elif result['type'] == 'video':
        await wait_message.delete() 
        await message.answer_video(video=result['media'], caption='Спасибо, что пользуетесь - @OKAsave_bot')
    elif result['type'] == 'image':
        await wait_message.delete() 
        await message.answer_photo(photo=result['media'], caption='Спасибо, что пользуетесь - @OKAsave_bot')
    elif result['type'] == 'carousel':
        await wait_message.delete() 
        for i in result['media']:
            await message.answer_document(document=i, caption='Спасибо, что пользуетесь - @OKAsave_bot')
