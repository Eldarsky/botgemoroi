from config import bot
from aiogram import types, Dispatcher



async def echo(message: types.Message):
    if message.text.isnumeric():
        await bot.send_message(message.from_user.id, int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)


def register_extra_handler(dp: Dispatcher):
    dp.register_message_handler(echo)