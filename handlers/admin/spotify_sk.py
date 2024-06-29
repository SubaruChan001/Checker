from aiogram import types
import requests, random, string
from loader import dp, bot
from data.config import PREFIX
import stripe

@dp.message_handler(commands=['sk'], commands_prefix=PREFIX)
async def sh1(message: types.Message):
  user = message.text[len('/sk '):]
  e = await message.reply(
    f'{message.from_user.first_name} wait i am checking  your sk key')
  sku = "https://api.stripe.com/v1/tokens"
  skd = "card[number]=5176170323019875&card[exp_month]=11&card[exp_year]=2026&card[cvc]=238"
  skh=  {
    "Host": "api.stripe.com",
    "content-length": "82",
    "sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"",
    "accept": "application/json, text/plain, */*",
    "content-type": "application/x-www-form-urlencoded",
    "sec-ch-ua-mobile": "?1",
    "authorization": f"Bearer {user}",
    "user-agent": "Mozilla/5.0 (Linux; Android 11; CPH1937) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "http://www.janawaldner.com",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "http://www.janawaldner.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q\u003d0.9,ar-EG;q\u003d0.8,ar;q\u003d0.7"
  }
  skr = requests.post(sku, headers=skh,data=skd)
  if "Expired API Key" in skr.text:
        return await e.edit_text(f"""
SK : <code>{user}</code>

║ RESPONSE OF SK
║ 💩 EXPIRED SK 💩

⌁ REQ BY : {message.from_user.first_name}
⌁ BOT BY :  @Was_B3
    """)
  elif "Invalid API Key provided" in skr.text:
    return await e.edit_text(f"""
SK : <code>{user}</code>

║ RESPONSE OF SK
║ INVALID KEY PROVIDED ❌

⌁ REQ BY : {message.from_user.first_name}
⌁ BOT BY : @Was_B3
    """)
  elif "rate_limit" in skr.text:
    stripe.api_key = user
    t = (stripe.Balance.retrieve())
    bl = (t["available"][0]["amount"])
    cur = (t["available"][0]["currency"])
    pe = (t["pending"][0]["amount"])
    ld = (t["livemode"])
    return await e.edit_text(f"""<b>
SK : <code>{user}</code>

║ RESPONSE OF SK
║ LIVE BUT RATE LIMIT⚠️
║ CURRENCY : {cur}
║ BALANCE : {bl}
║ PENDING : {pe}

⌁ REQ BY : {message.from_user.first_name}
⌁ BOT BY : @Was_B3
</b>""")
  elif """{
  "error": {""" in skr.text:
      req = (skr.json()["error"]["code"])
      if req == "testmode_charges_only":
          return await e.edit_text(f"""<b>
SK : <code>{user}</code>

║ RESPONSE OF SK
║ TESTMODE CHARGE ONLY 

⌁ REQ BY : {message.from_user.first_name}
⌁ BOT BY : @Was_B3
</b>""")
      else:
        stripe.api_key = user
        t = (stripe.Balance.retrieve())
        bl = (t["available"][0]["amount"])
        cur = (t["available"][0]["currency"])
        pe = (t["pending"][0]["amount"])
        ld = (t["livemode"])
        print(ld)
        if ld == True:
            
            return await e.edit_text(f"""<b>
SK : <code>{user}</code>

║ RESPONSE OF SK
║ LIVE CHARGED ✅
║ CURRENCY : {cur}
║ BALANCE : {bl}
║ PENDING : {pe}

⌁REQ BY : {message.from_user.first_name}
⌁ BOT BY : @Was_B3
</b>""")

def getRandomString(length):
  pool = string.ascii_lowercase + string.digits
  return "".join(random.choice(pool) for i in range(length))


def getRandomText(length):
  return "".join(random.choice(string.ascii_lowercase) for i in range(length))


def generate():
  nick = getRandomText(8)
  passw = getRandomString(12)
  email = nick + "@" + "gmail" + ".com"

  headers = {
    "Accept-Encoding": "gzip",
    "Accept-Language": "en-US",
    "App-Platform": "Android",
    "Connection": "Keep-Alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "spclient.wg.spotify.com",
    "User-Agent": "Spotify/8.6.72 Android/29 (SM-N976N)",
    "Spotify-App-Version": "8.6.72",
    "X-Client-Id": getRandomString(32)
  }

  payload = {
    "creation_point": "client_mobile",
    "gender": "male" if random.randint(0, 1) else "female",
    "birth_year": random.randint(1990, 2000),
    "displayname": nick,
    "iagree": "true",
    "birth_month": random.randint(1, 11),
    "password_repeat": passw,
    "password": passw,
    "key": "142b583129b2df829de3656f9eb484e6",
    "platform": "Android-ARM",
    "email": email,
    "birth_day": random.randint(1, 20)
  }

  r = requests.post(
    'https://spclient.wg.spotify.com/signup/public/v1/account/',
    headers=headers,
    data=payload)

  if r.status_code == 200:
    if r.json()['status'] == 1:
      text = f"""<b>
Auto Spotify Created! ✅
♪ Premium-»  🤨
♪ Email-» <b>{email}</b>
♪ Password-»<code>{passw}</code>
</b>"""

      return (text)
    else:
      #Details available in r.json()["errors"]
      #print(r.json()["errors"])
      return (False, "Could not create the account, some errors occurred")
  else:
    return (False,
            "Could not load the page. Response code: " + str(r.status_code))


@dp.message_handler(commands=['spotify'], commands_prefix=PREFIX)
async def ch(message: types.Message):
  return await message.reply(generate())
