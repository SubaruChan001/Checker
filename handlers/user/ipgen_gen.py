from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp

from aiogram import *

import random


PREFIX = "!/."

import re, os
import concurrent.futures

import requests




def checkLuhn(cardNo):


  nDigits = len(cardNo)
  nSum = 0
  isSecond = False

  for i in range(nDigits - 1, -1, -1):
    d = ord(cardNo[i]) - ord('0')

    if (isSecond == True):
      d = d * 2

    # We add two digits to handle
    # cases that make two digits after
    # doubling
    nSum += d // 10
    nSum += d % 10

    isSecond = not isSecond

  if (nSum % 10 == 0):
    return True
  else:
    return False


def cc_gen(
  cc,
  mes='x',
  ano='x',
  cvv='x',
  amount='x',
):
  if amount != 'x':
    amount = int(amount)
  else:
    amount = 15
  genrated = 0
  ccs = []
  while (genrated < amount):
    genrated += 1
    s = "0123456789"
    l = list(s)
    random.shuffle(l)
    result = ''.join(l)
    result = cc + result
    if cc[0] == "3":
      ccgen = result[0:15]
    else:
      ccgen = result[0:16]
    if mes == 'x':
      mesgen = random.randint(1, 12)
      if len(str(mesgen)) == 1:
        mesgen = "0" + str(mesgen)
    else:
      mesgen = mes
    if ano == 'x':
      anogen = random.randint(2021, 2029)
    else:
      anogen = ano
    if cvv == 'x':
      if cc[0] == "3":
        cvvgen = random.randint(1000, 9999)
      else:
        cvvgen = random.randint(100, 999)
    else:
      cvvgen = cvv
    # if not x: continue

    if ccgen and not checkLuhn(ccgen):
      pass
    if (ccgen, mesgen, anogen, cvvgen):
      lista = "<code>" + str(ccgen) + "|" + str(mesgen) + "|" + str(
        anogen) + "|" + str(cvvgen) + "</code>"
      ccs.append(lista)

  return ccs

from main import BINS_DICT
@dp.message_handler(commands=['gen', 'GEN'], commands_prefix=PREFIX)
async def igfgnfokc(message: types.Message):



  text = message.text[len('/gen '):]
  if len(text) < 6:
    await message.answer("Invalid bin.")
    return
  BIN = text[0:5]
  try:
    rem = BINS_DICT[BIN]
  except:
    return await message.answer("Invalid bin.")
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
  cards = ''
  from ccgen import okcc
  try:
    dd = message.text.split(" ")[1]
    dd1 = int(message.text.split(" ")[2])
  except:
    return await message.reply("cc gen format /gen bin amount")
  for x in range(dd1):
    cards += okcc(dd) + "\n"
  mess = f"""
<b> ————Bin Details———— </b>

Type -»<b>{type}</b>

Brand -»<b>{brand}</b>

bank data -»<b>{bank}</b>

Country -»<b>{country}{flag}</b>

<b>Cards</b>: 

{cards}

"""



  await message.answer(mess)




@dp.message_handler(commands=['ipgen'], commands_prefix=PREFIX)

async def cdgh(message: types.Message):

  kk = await message.reply("<b> Generating Please Wait :) (: </b>")
  try:
    user = int(message.text[len('/ipgen '):])
    if user > 100000:
      return await message.reply("maxx limit is 100000")

    def ips():
      ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
      return ip

    text = ""
    for x in range(int(user)):
      with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(ips)
        return_value = future.result()

        text += f"{return_value}\n"

    listf = f"{user}_ips_TSM.txt"
    with open(listf, "a") as f:
      f.write(f"{text}\n")

    video = open(listf, "rb")
    await kk.delete()
    await message.reply_document(document=video,
                                 caption=f"""
<b>Success! Done ✅! </b>

Amount: <b>{user}</b>

Generated By : <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>

Bot by : <a href="tg://user?id= 1226290399"><b>⏤͟͞B3</b></a>

""")

    os.remove(listf)
  except:
    await message.reply('invalid Format \ntry: /ipgen (amount)')




@dp.message_handler(commands=['fix'], commands_prefix=PREFIX)

async def cdsdgh(message: types.Message):

  try:
    all_cards = message.text.split('\n')
    for x in all_cards:
      cc = x.split(': ')[0]
      cc1 = x.split(': ')[1]
      ccq = "'" + cc + "'"
      ccw = ":'" + cc1 + "',"
      with open("v.txt", "a") as f:
        f.write(f"{ccq}{ccw}\n")

    f = open("v.txt", "r")
    ccj = f.read()
    await message.reply(f"<code>'{ccj[7:]}</code> ",
                        disable_web_page_preview=True)
    f.close()
    os.remove("v.txt")

  except:
    await message.reply('Provide Me a Valid Headers to Fix')
