import json
import string
from aiogram import types
from create_bot import dp


@dp.message_handler()
async def message_filter(message: types.message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('blackList.json')))) != set():
        await message.reply('Такое слово запрещено')
        await message.delete()
