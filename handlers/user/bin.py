
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from loader import dp
from main import ok
from data.config import PREFIX
import requests
from aiogram import  types
from main import BINS_DICT


@dp.message_handler(commands=['bin'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):
  try:


    cc = message.text[len('/bin '):]
    splitter = cc.split('|')
    BIN = splitter[0]
    BIN = cc[:6]
    fbin = cc[:6]
    session = requests.session()
    bin = BINS_DICT[fbin]
    try:
      brand = bin["vendor"].upper()
    except:
      brand = "N/A"
    try:
      type = bin["type"].upper()
    except:
      type = "N/A"
    try:
      level = bin["level"].upper()
    except:
      level = "N/A"
    try:
      bank = bin["bank_name"].upper()
    except:
      bank = "N/A"
    try:
      country = bin["country"].upper()
    except:
      country = "N/A"
    try:
      flag = bin["flag"]
    except:
      flag = "N/A"


    INFO = f'''
<b>Valid {BIN}</b> ✅

<b> ————Bin Details———— </b>

Brand -» <b>{brand}</b>
Type -» <b>{type} {level}</b>
Bank  -»<b>{bank}</b>
Country -»<b>{country} {flag}</b>

Checked by -» <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> <b>[{ok(message.from_user.id)}]</b>
  '''
    await message.reply(INFO)
  except:
    return await message.reply("❌ INVALID BIN  ❌ ")


