from aiogram import types, Dispatcher
from aiogram.types import ParseMode
from create_bot import dp, bot
from Keyboards import kb_client
import requests


@dp.message_handler(commands=['start'])
async def command_start(message: types.message):
    await bot.send_message(message.from_user.id, f'👋Здравствуйте, {message.from_user.username}! \nЯ <b>CurrencyBot'
                                                 f'</b>, помогу узнать вам про новости, курсы валют и многое '
                                                 f'другое.\nДля просмотра помощи отправьте команду /help',
                           parse_mode=ParseMode.HTML, reply_markup=kb_client)


@dp.message_handler(commands=['help'])
async def actual_weather(message: types.Message):
    await message.answer('Бот умеет следующие команды:\n/Новости /Конвертер /Валюта /Ценные бумаги /Криптовалюта '
                         '/Металлы')


@dp.message_handler(commands=['Новости'])
async def actual_news(message: types.Message):
    await message.answer('Хорошие новости - новостей нет!')


@dp.message_handler(commands=['Конвертер'])
async def actual_news(message: types.Message):
    await message.answer('Введите исходную валюту, валюту в которую нужно конвертировать и сумму конвертации через '
                         'запятую(Пример: USD, RUB, 1000)')
    text = message.text
    print(text)
    val1, val2, count = text.split(',')
    if val1 and val2 != 'USD' or 'EUR':
        await message.answer('Вы ввели неверную валюту', val1, val2, count)
    else:
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        cur = data['Valute'][f'{val1}']['Value']
        cur2 = data['Valute'][f'{val2}']['Value']
        await message.answer(f'{count} {val1} -> {cur / cur2 * count} {val2}', val1, val2, count)


@dp.message_handler(commands=['Валюта'])
async def actual_news(message: types.Message):
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    usd = data['Valute']['USD']['Value']
    eur = data['Valute']['EUR']['Value']
    await message.answer(f'USD = {usd}₽\nEUR = {eur}₽')


@dp.message_handler(commands=['Ценные бумаги'])
async def actual_news(message: types.Message):
    await message.answer('Хорошие новости - новостей нет!')


@dp.message_handler(commands=['Криптовалюта'])
async def actual_news(message: types.Message):
    await message.answer('Хорошие новости - новостей нет!')


@dp.message_handler(commands=['Металлы'])
async def actual_news(message: types.Message):
    await message.answer('Хорошие новости - новостей нет!')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_start, commands=['help'])
    dp.register_message_handler(command_start, commands=['Новости'])
    dp.register_message_handler(command_start, commands=['Конвертер'])
    dp.register_message_handler(command_start, commands=['Валюта'])
    dp.register_message_handler(command_start, commands=['Ценные бумаги'])
    dp.register_message_handler(command_start, commands=['Криптовалюта'])
    dp.register_message_handler(command_start, commands=['Металлы'])
