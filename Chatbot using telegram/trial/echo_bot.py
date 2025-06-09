from aiogram import Bot, Dispatcher, types, F
from dotenv import load_dotenv
import os
import logging
import asyncio

load_dotenv()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
dp = Dispatcher()

@dp.message(F.text.in_(['/start', '/help']))
async def command_start_handler(message: types.Message):
    await message.reply('Hi! \n I am an Echo Bot! \n Powered by aiogram')

@dp.message()
async def echo(message: types.Message):
   await message.reply(message.text)
   
if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))