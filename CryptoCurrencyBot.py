from aiogram.utils import executor
from create_bot import dp
from Handlers import client, admin, other


async def on_startup(_):
    print('Бот запущен')

client.register_handlers_client(dp)
other.message_filter(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
