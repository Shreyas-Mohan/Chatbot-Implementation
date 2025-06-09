from aiogram import Bot, Dispatcher, types, F
from dotenv import load_dotenv
import os
import asyncio
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv('GOOGLE_API_KEY'),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
dp = Dispatcher()

class Reference:             # class to store the last assistant response for context
   def __init__(self)->None: 
      self.response= ''
reference = Reference()

@dp.message(F.text.in_(['/start']))
async def welcome(message: types.Message):
   await message.reply('Hi\n I am a Cricket Chatbot! Created by Shreyas. \n How can i assist you ?')

@dp.message(F.text.in_(['/clear']))
async def clear(message: types.Message):
   reference.response=''
   await message.reply("I've cleared the past conversation and context")

@dp.message()
async def main_bot(message: types.Message):
   response=client.chat.completions.create(
      model='gemini-2.5-flash-preview-05-20',
      messages=[
         {'role': 'assistant', 'content': reference.response},
         {'role': 'user', 'content':message.text}         
      ]
   )
   reference.response = response.choices[0].message.content             # Stores the assistant's reply for use as context in the next turn.
   await bot.send_message(chat_id=message.chat.id, text=reference.response)
   
if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))