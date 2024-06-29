
from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp
from aiogram import *
PREFIX = "!/."
import requests
@dp.message_handler(commands=["hma"], commands_prefix=PREFIX)
async def kk(message: types.Message):
    button1 = InlineKeyboardButton(
        text="GET-KEY-HERE", url="tg://user?id=1226290399")
    keyboard_inline = InlineKeyboardMarkup().add(button1)
    try:

        fff = message.text[len('/key '):]
        await message.delete()
        dd = await message.answer("<code>checking...</code>")
        url = f"https://api.nqduv.dev/checkkeyhma.php?key={fff}"
        me = requests.get(url)
        m = me.json()

        ip = m["auto Renew"]
        score = m["subscription"]
        cm = m["created"]
        cc = m["expires"]
        return await dd.edit_text(f"""
Key =  <b> <a href='https://t.me/Noir_Tempest_001'>* Hidden *</a> </b>
subscription = <b>{score}</b>
created = <b>{cm}</b>
expires = <b>{cc}</b>
auto Renew = <b>{ip}</b>
""", disable_web_page_preview=True, reply_markup=keyboard_inline)

    except:
        return await dd.edit_text(f"""
        <b>🚫 DEAD KEY 🚫</b>
""")










