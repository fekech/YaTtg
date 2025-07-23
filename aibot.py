import asyncio
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

bot = Bot(token="7700864323:AAHlmKVM1X4KI-FaPv82cf4sap-y2kUThus")

dp = Dispatcher()

@dp.message(Command("start"))
async def command_start_handler(message: Message):
    await message.answer("Привет напиши команду /adduser Login:Password что бы добавить себя в пул выгрузов сообщений из яндекс почты \n\nВАЖНО! \n\nБот для работы требует пароль и логин от Яндекс Почты!\n\nВАЖНО! \n")

@dp.message(Command("adduser"))
async def return_id_chat_id_yandex(message: Message):
	await message.reply("Ваш chat ID : "+str(message.chat.id)+"\nЛогин и пароль Яндекс Почты : "+str(message.text))

async def send_message(chatd_id=message.chat.id)


async def main():
    await dp.start_polling(bot)

asyncio.run(main())