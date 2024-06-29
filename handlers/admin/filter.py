from aiogram.utils.exceptions import Throttled
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from data.config import PREFIX
from loader import dp
from main import ok
import re


@dp.message_handler(commands=['clean'], commands_prefix=PREFIX)
async def mas2(message: types.Message):
  kk = await message.reply('<b>wait i am little busy </b>')
  all_cards = message.text.split('\n')
  cards = ""
  for cc in all_cards:
    try:

      x = re.findall(r'\d+', cc)
      ccn = x[0]
      mm = x[1]
      yy = x[2]
      cvv = x[3]
      if mm.startswith('2'):
        mm, yy = yy, mm
      if len(mm) >= 3:
        mm, yy, cvv = yy, cvv, mm
      if len(ccn) < 15 or len(ccn) > 16:
        pass
      else:
        
        cards += f"{ccn}|{mm}|{yy}|{cvv}\n"
    except:
      pass

  try:
    await kk.edit_text(f"""<code>{cards}</code>""")
  except Exception as e:
    await kk.edit_text(e)


