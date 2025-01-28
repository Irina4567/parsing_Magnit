from os import getenv
from async_main import collect_data
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiofiles import os

import os as globalOs

bot = Bot(globalOs.environ.get('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['Moscow']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer('Please select a City', reply_markup=keyboard)


@dp.message_handler(Text(equals='Moscow'))
async def moscow_city(message: types.Message):
    await message.answer('Please waiting...')
    chat_id = message.chat.id
    await send_data(city_code='2398', chat_id=chat_id)


async def send_data(city_code='', chat_id=''):
     file = await collect_data(city_code=city_code)
#     print(file)
    await bot.send_message(chat_id, file)


if __name__ == '__main__':
    executor.start_polling(dp)