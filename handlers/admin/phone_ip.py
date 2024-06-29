import requests
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp
from aiogram import types
from data.config import PREFIX


@dp.message_handler(commands=['phone'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):
  phone = message.text[len('/phone '):]
  if not phone or not phone.startswith('+') or len(phone) < 10:
    await message.reply("invalid Phone Number")
    return
  key = "fe65b94e78fc2e3234c1c6ed1b771abd"
  api = ("http://apilayer.net/api/validate?access_key=" + key + "&number=" +
         phone + "&country_code=&format=1")
  output = requests.get(api)
  data = output.json()
  text = "Phone Number Information\n"
  for x in data:
    text += str(x.replace('_', ' ').title()) + " : " + str(data[x]) + "\n"
  return await message.reply(text)


def find_between(data, first, last):
  try:
    start = data.index(first) + len(first)
    end = data.index(last, start)
    return data[start:end]
  except ValueError:
    return None