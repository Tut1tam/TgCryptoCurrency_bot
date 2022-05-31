from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/News')
b2 = KeyboardButton('/Converter')
b3 = KeyboardButton('/Currency')
b4 = KeyboardButton('/Securities')
b5 = KeyboardButton('/Cryptocurrency')
b6 = KeyboardButton('/Precious_metals')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(b1).insert(b4).add(b2).insert(b5).add(b3).insert(b6)
