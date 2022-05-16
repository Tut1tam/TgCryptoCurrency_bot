from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Новости')
b2 = KeyboardButton('/Конвертер')
b3 = KeyboardButton('/Валюта')
b4 = KeyboardButton('/Ценные бумаги')
b5 = KeyboardButton('/Криптовалюта')
b6 = KeyboardButton('/Металлы')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(b1).insert(b4).add(b2).insert(b5).add(b3).insert(b6)
