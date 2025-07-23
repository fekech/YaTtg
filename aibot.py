import asyncio
from os import getenv
import auth

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

bot = Bot(token="7700864323:AAHlmKVM1X4KI-FaPv82cf4sap-y2kUThus")

dp = Dispatcher()

@dp.message(Command("start"))
async def command_start_handler(message: Message):
    await message.answer("Привет напиши команду /adduser filyakert(Login):746351(password) что бы добавить себя в пул выгрузов сообщений из яндекс почты \n\nВАЖНО! \n\nБот для работы требует пароль и логин от Яндекс Почты! не нужно писать после логина @yandex.ru только сломаешь бота ;D\n\nВАЖНО! \n")

@dp.message(Command("adduser"))
async def return_id_chat_id_yandex(message: Message):
	await message.reply("Ваш chat ID : "+str(message.chat.id)+"\n\nЛогин и пароль Яндекс Почты \nLogin : "+message.text.split(':')[0].split(' ')[1]+'@yandex.ru'+'\nPassword : '+message.text.split(':')[1])
	auth.UploadDb(message.chat.id,message.text.split(':')[0].split(' ')[1]+'@yandex.ru',message.text.split(':')[1])
	print(auth.LoadDb(message.chat.id))
	
async def main():
    await dp.start_polling(bot)

asyncio.run(main())