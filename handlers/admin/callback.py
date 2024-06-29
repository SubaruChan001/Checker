from aiogram import *
from data.config import OWNER_NAME, OWNER_LINK, GROUP, CHANNEL
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from main import ok
from loader import dp

PREFIX = "!/."

#===========================================================================handler ========================================================================


@dp.callback_query_handler(text=["b3", "shopify", "Payeezy", "stripe", "Cybersource", "Square"])
async def process_cart(call: types.CallbackQuery):

  original = call.message.reply_to_message.from_user.id
  cc = call.get_current()
  id = cc.from_user.id
  if id == original:
    if call.data == "b3":
      button3 = InlineKeyboardButton(text="🔙", callback_data="free")
      button4 = InlineKeyboardButton(text="🔚", callback_data="close")
      keyboard_inline = InlineKeyboardMarkup().add(
        button3, button4)
      await call.message.edit_text(f"""<b>All Gates Are Made With Love And Hard Work :) By {OWNER_NAME}

Braintree  $5
/ch ✅ Active | 02/25/24

Braintree Auth
/chk ✅ Active | 02/25/24
</b>
[+] Adding more...

<b> Bot made by: <a href='{OWNER_LINK}'> {OWNER_NAME} </a> </b>""",
                                   reply_markup=keyboard_inline,
                                   disable_web_page_preview=True)
    elif call.data == "shopify":
      return await call.message.edit_text(f"""<b>
[~] Soon...
</b>
<b> Bot made by: <a href='{OWNER_LINK}'> {OWNER_NAME} </a> </b>""",
                                   reply_markup=keyboard_inline,
                                   disable_web_page_preview=True)
    elif call.data == "Payeezy":
      return await call.message.edit_text(f"""<b>
[~] Soon...
</b>
<b> Bot made by: <a href='{OWNER_LINK}'> {OWNER_NAME} </a> </b>""",
                                   reply_markup=keyboard_inline,
                                   disable_web_page_preview=True)
    elif call.data == "stripe":
      return await call.message.edit_text(f"""<b>
[~] Soon...
</b>
<b> Bot made by: <a href='{OWNER_LINK}'> {OWNER_NAME} </a> </b>""",
                                   reply_markup=keyboard_inline,
                                   disable_web_page_preview=True)
    elif call.data == "Cybersource":
      return await call.message.edit_text(f"""<b>
[~] Soon...
</b>
<b> Bot made by: <a href='{OWNER_LINK}'> {OWNER_NAME} </a> </b>""",
                                   reply_markup=keyboard_inline,
                                   disable_web_page_preview=True)
    elif call.data == "Square":
      return await call.message.edit_text(f"""<b>
[~] Soon...
</b>
<b> Bot made by: <a href='{OWNER_LINK}'> {OWNER_NAME} </a> </b>""",
                                   reply_markup=keyboard_inline,
                                   disable_web_page_preview=True)
  else:
    return await call.answer(
      "❌ Access denied, only the user who used the command can navigate the buttons. ❗️",
      show_alert=True)

@dp.callback_query_handler(text=["free", "paid", "close", "other", "back"])
async def process_cart(call: types.CallbackQuery):

  original = call.message.reply_to_message.from_user.id
  cc = call.get_current()
  id = cc.from_user.id
  if id == original:

    if call.data == "free":
      b3 = InlineKeyboardButton(text="Braintree", callback_data="b3")
      shopify = InlineKeyboardButton(text="Shopify", callback_data="shopify")
      Payeezy = InlineKeyboardButton(text="Payeezy", callback_data="Payeezy")
      Stripe = InlineKeyboardButton(text="Stripe", callback_data="stripe")
      Cybersource = InlineKeyboardButton(text="Cybersource", callback_data="Cybersource")
      Square = InlineKeyboardButton(text="Square", callback_data="Square")
      button3 = InlineKeyboardButton(text="🔙", callback_data="back")
      button4 = InlineKeyboardButton(text="🔚", callback_data="close")

      keyboard_inline = InlineKeyboardMarkup().add(b3,shopify).add(Stripe,Square).add(Cybersource,Payeezy).add(
        button3, button4)
      await call.message.edit_text(f"""
<b>all gates are made with love and hard work :) by {OWNER_NAME}

Usage :
<code>/ch 4647...6215|11|2024|630</code>
</b>
[~] Adding more...

<b> Bot made by: <a href='{OWNER_LINK}'> {OWNER_NAME} </a> </b>""",
                                   reply_markup=keyboard_inline,
                                   disable_web_page_preview=True)
      
    elif call.data == "paid":

      button1 = InlineKeyboardButton(text="Normal gates", callback_data="free")
      button3 = InlineKeyboardButton(text="🔙", callback_data="back")
      button4 = InlineKeyboardButton(text="🔚", callback_data="close")
      keyboard_inline = InlineKeyboardMarkup().add(button1).add(
        button3, button4)

      await call.message.edit_text(f"""<b>
[~] Soon...
</b>
<b> Bot made by: <a href='{OWNER_LINK}'> {OWNER_NAME} </a> </b>""",
                                   reply_markup=keyboard_inline,
                                   disable_web_page_preview=True)

    elif call.data == "close":
      await call.message.edit_text("Enjoy Baby 🧸.")

    elif call.data == "back":
      button1 = InlineKeyboardButton(text="Normal gates", callback_data="free")
      button2 = InlineKeyboardButton(text="Mass gates", callback_data="paid")
      button3 = InlineKeyboardButton(text="🔙", callback_data="back2")
      button4 = InlineKeyboardButton(text="🔚", callback_data="close")
      keyboard_inline = InlineKeyboardMarkup().add(button1).add(button2).add(
        button3, button4)

      await call.message.edit_text(f"""
        <b>
Hello, it seems to me that you are interested in my commands, you can explore by pressing any of the buttons
<b>User type = {call.message.reply_to_message.from_user.username}</b> ({ok(call.message.reply_to_message.from_user.id)})
Bot made by: <a href='{OWNER_LINK}'> {OWNER_NAME} </a> </b>""",
                                   reply_markup=keyboard_inline,
                                   disable_web_page_preview=True)

    elif call.data == "other":

      button2 = InlineKeyboardButton(text="🔙", callback_data="back2")
      button3 = InlineKeyboardButton(text="🔚", callback_data="close")
      keyboard_inline = InlineKeyboardMarkup().add(button2, button3)

      await call.message.edit_text(f"""
<b>
/status to check group status
/check check your own id
/admins

/clean (text to extract cc)
/bin xxxxxx  to check bin 
/fake or /us generat fake data
/ipgen (amount) generate ip list
/gen cc gen
/hma HMA key checker
/phone (number) 
/fix (headers) headers editor
/ip (check ip risk score)
/sk sk_live_xxx to check sk keys (with balance)
/buy to buy bot 
/inf to check group id 

[proxy cmds]

/http
/socks4
/socks5

[translator]
/tr (language_code) text
/voice (language_code) text
/code 

[admin cmds]

/adduser
/deluser
/addadmin
/deladmin
/approve
/revoke

</b>
<b> Bot made by: <a href='{OWNER_LINK}'> {OWNER_NAME} </a> </b>""",
                                   reply_markup=keyboard_inline,
                                   disable_web_page_preview=True)

  else:

    return await call.answer(
      "❌ Access denied, only the user who used the command can navigate the buttons. ❗️",
      show_alert=True)
