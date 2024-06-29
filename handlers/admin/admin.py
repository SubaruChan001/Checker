from database import *
from data.config import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot
from aiogram import types
from main import ok

from data.config import PREFIX


@dp.message_handler(commands=['status'], commands_prefix=PREFIX)
async def helpstr(message: types.Message):

  group = str(message.chat.id)
  paid = open("files/group.txt").read().splitlines()
  ug = message.chat.type
  if "supergroup" in ug or "group" in ug:
    if group in paid:
      text = f"""
Group Name = <b>{message.chat.full_name}</b>
Group Id = <code>{message.chat.id}</code>
Status = Active
"""
      await message.reply(text)
    else:
      text = f"""
Group Name = <b>{message.chat.full_name}</b>
Group Id = <code>{message.chat.id}</code>
Status = Not Allowed
"""
      await message.reply(text)
      await message.reply(
        "<b> This Chat IS Not Allowed Contact My master @Noir_Tempest_001  I Am Leaving :)</b>"
      )
      await bot.leave_chat(group)

  else:
    await message.reply("""Cannot Use this command in Private Chat""",
                        disable_web_page_preview=True)


@dp.message_handler(commands=['check'], commands_prefix=PREFIX)
async def infokfc(message: types.Message):





  if message.reply_to_message:
    user_id = message.reply_to_message.from_user.id
    is_bot = message.reply_to_message.from_user.is_bot
    username = message.reply_to_message.from_user.username
    first = message.reply_to_message.from_user.first_name
    id = message.reply_to_message.from_user.id
    username = message.reply_to_message.from_user.username
  else:
    id = message.from_user.id
    username = message.from_user.username
    user_id = message.from_user.id
    is_bot = message.from_user.is_bot
    username = message.from_user.username
    first = message.from_user.first_name



  user_id = user_id

  if user_id ==  1226290399:
    chcc = "OWNER"

  else:
    chcc = ok(user_id)

  try:
    text = f"""<b>🆔 ID:</b> <code>{user_id}</code>
<b>👱 NAME:</b><a href="tg://user?id={user_id}">{first}</a>
<b>🌐 Username:</b> @{username}
<b>🤖 IS bot = </b> {is_bot}
<i>Type </i> = <b>{chcc}</b>
<i>Is User </i> = <b>{(check_user(id))}</b>
<i>Is Admin </i> = <b>{(check_admin(id))}</b>
<i>Expire on </i> = <b>{(fetch_expiry_date(id))}</b>
<i>Days_left </i> = <b>{check_expiry_days(id)}</b>
"""
    await message.reply(text)

  except:
    text = f"""
<i>Type </i> = <b>{ok(id)}</b>
<i>User Name </i> = <b>{username}</b>
<i>User Id </i> = <code>{id}</code>
<i>User </i> = <b>{(check_user(id))}</b>
<i>Admin </i> = <b>{(check_admin(id))}</b>
<i>Expire on </i> = <b>"Buy A Plan First"</b>
<i>Days_left </i> = <b>No Active Plan</b>
"""
    await message.reply(text)


@dp.message_handler(commands=['approve'], commands_prefix=PREFIX)
async def infokfc(message: types.Message):

  guid = str(message.chat.id)
  m = str(message.from_user.id)
  ug = message.chat.type
  if "supergroup" in ug or "group" in ug:
    if str("1226290399") in m:
      guid = f'{message.chat.id}'
      gps = open("files/group.txt").read().splitlines()

      if guid in gps:
        await message.reply(
          f'''  {message.chat.full_name}  <b> is already in Authorised </b>''')

      else:
        with open("files/group.txt", "a") as f:
          f.write(f"{guid}\n")

        await message.reply(
          f''' <b>✅ Success authorised  to {message.chat.full_name}</b>''')

    else:

      op = await message.reply("""You Are Not Allowed To use This Command""",
                               disable_web_page_preview=True)

  else:
    await message.reply("""Cannot Use this command in Private Chat""",
                        disable_web_page_preview=True)


@dp.message_handler(commands=['revoke'], commands_prefix=PREFIX)
async def igfgnfokc(message: types.Message):

  m = str(message.from_user.id)

  ug = message.chat.type
  if "supergroup" in ug or "group" in ug:
    if str("1226290399") in m:

      guid = str(message.chat.id)

      gps = open("files/group.txt").read().splitlines()

      if guid not in gps:
        await message.reply(f'''<b>Not Found In Authorised Chats </b>''')
        await bot.leave_chat(message.chat.id)

      else:
        await message.reply(
          f''' <b>Revoked Access of {message.chat.full_name}</b>''')
        await bot.leave_chat(guid)

        word = f'{message.chat.id}'

        with open("files/group.txt", "r") as fp:
          lines = fp.readlines()
        with open("files/group.txt", "w") as fp:
          for line in lines:
            if line.strip("\n") != word:
              fp.write(line)
              fp.close()

    else:

      op = await message.reply("""You Are Not Allowed To use This Command """,
                               disable_web_page_preview=True)

  else:
    await message.reply("""Cannot Use this command in Private Chat""",
                        disable_web_page_preview=True)


import time


@dp.message_handler(commands=['addadmin'], commands_prefix=PREFIX)
async def infokfc(message: types.Message):

  try:

    query = message.text[len('/addadmin '):]

    id = message.from_user.id

    if check_admin(id) == True:

      if len(query) != 0:
        user_id = query
      else:
        try:
          user_id = message.reply_to_message.from_user.id
        except:
          return await message.reply("invalid id provided")
      adminid = user_id
      km = await bot.get_chat(user_id)
      username = km.username

      alredy = alredyadmin()

      if int(user_id) in alredy:
        return await message.reply(
          f"""<b>  <a href='tg://user?id={user_id}'>{username}</a> </b> is Alredy Admin""",
          disable_web_page_preview=True)

      if int(user_id) == OWNERID:
        return await message.reply("You cannnot promote Super User 😝😝")

      create_admin(adminid)
      create_user_lifetime(adminid)
      return await message.reply(
        f"""<b> Added <a href='tg://user?id={user_id}'>{username}</a> </b> as Admin""",
        disable_web_page_preview=True)

    else:

      await message.reply("""You Are Not Allowed To use This Command """,
                          disable_web_page_preview=True)

  except Exception as E:
    await message.reply(E)


import time


@dp.message_handler(commands=['deladmin'], commands_prefix=PREFIX)
async def infokfc(message: types.Message):

  query = message.text[len('/deladmin '):]
  id = message.from_user.id

  if check_admin(id) == True:

    if len(query) != 0:
      user_id = query
    else:
      try:
        user_id = message.reply_to_message.from_user.id
      except:
        return await message.reply("invalid id provided")

    km = await bot.get_chat(user_id)
    username = km.username

    alredy = alredyadmin()

    if int(user_id) not in alredy:
      return await message.reply(
        f"""<b>  <a href='tg://user?id={user_id}'>{username}</a> </b> this User not Found in Admin list""",
        disable_web_page_preview=True)

    if int(user_id) == OWNERID:
      return await message.reply(f"You cannnot demote Super User 😝😝")

    userid = user_id
    delete_specific_AdminData(userid)
    delete_specific_UserData(userid)
    return await message.reply(
      f"""<b> Deleted <a href='tg://user?id={user_id}'>{username}</a> </b> from Admin""",
      disable_web_page_preview=True)
  else:

    await message.reply("""You Are Not Allowed To use This Command """,
                        disable_web_page_preview=True)


@dp.callback_query_handler(
  text=["1 days", "7 days", "1 month", "3 months", "Lifetime"])
async def process_cart(call: types.CallbackQuery):

  if call.data == "1 days":

    cc = call.get_current()

    id = cc.from_user.id
    if check_admin(id) == True or check_owner(id) == True:

      userid = call.message.reply_to_message.text[len('/adduser '):]

      km = await bot.get_chat(userid)
      username = km.username
      user_id = int(km.id)

      create_user_test(userid)

      return await call.message.edit_text(
        f"""<b> Added <a href='tg://user?id={user_id}'>{username}</a> in</b> Test  Plan""",
        disable_web_page_preview=True)

    else:

      await call.answer("You Are ot Allowed To click Here 😂.", show_alert=True)

  if call.data == "7 days":
    cc = call.get_current()

    id = cc.from_user.id
    if check_admin(id) == True or check_owner(id) == True:

      userid = call.message.reply_to_message.text[len('/adduser '):]

      km = await bot.get_chat(userid)
      username = km.username
      user_id = int(km.id)

      create_user_7days(userid)

      return await call.message.edit_text(
        f"""<b> Added <a href='tg://user?id={user_id}'>{username}</a> in</b> 7days  Plan""",
        disable_web_page_preview=True)

    else:

      await call.answer("You Are ot Allowed To click Here 😂.", show_alert=True)

  if call.data == "1 month":
    cc = call.get_current()

    id = cc.from_user.id
    if check_admin(id) == True or check_owner(id) == True:

      userid = call.message.reply_to_message.text[len('/adduser '):]

      km = await bot.get_chat(userid)
      username = km.username
      user_id = int(km.id)

      create_user_1month(userid)

      return await call.message.edit_text(
        f"""<b> Added <a href='tg://user?id={user_id}'>{username}</a> in</b> 1month  Plan""",
        disable_web_page_preview=True)

    else:

      await call.answer("You Are ot Allowed To click Here 😂.", show_alert=True)

  if call.data == "3 months":
    cc = call.get_current()

    id = cc.from_user.id
    if check_admin(id) == True or check_owner(id) == True:

      userid = call.message.reply_to_message.text[len('/adduser '):]

      km = await bot.get_chat(userid)
      username = km.username
      user_id = int(km.id)

      create_user_3months(userid)

      return await call.message.edit_text(
        f"""<b> Added <a href='tg://user?id={user_id}'>{username}</a> in</b> 3 months  Plan""",
        disable_web_page_preview=True)

    else:

      await call.answer("You Are ot Allowed To click Here 😂.", show_alert=True)

  if call.data == "Lifetime":
    cc = call.get_current()

    id = cc.from_user.id
    if check_admin(id) == True or check_owner(id) == True:

      userid = call.message.reply_to_message.text[len('/adduser '):]

      km = await bot.get_chat(userid)
      username = km.username
      user_id = int(km.id)

      create_user_lifetime(userid)

      return await call.message.edit_text(
        f"""<b> Added <a href='tg://user?id={user_id}'>{username}</a> in</b> lifetime  Plan""",
        disable_web_page_preview=True)

    else:

      await call.answer("You Are ot Allowed To click Here 😂😂", show_alert=True)


import time


@dp.message_handler(commands=['adduser'], commands_prefix=PREFIX)
async def infokfc(message: types.Message):
  query = message.text[len('/adduser '):]

  try:
    km = await bot.get_chat(query)
    username = km.username
    user_id = int(km.id)
    id = (message.from_user.id)
    if check_admin(id) == True or check_owner(id) == True:
      item1 = InlineKeyboardButton(text="Test", callback_data="Test")
      item2 = InlineKeyboardButton(text="7 days", callback_data="7 days")
      item3 = InlineKeyboardButton(text="1 month", callback_data="1 month")
      item4 = InlineKeyboardButton(text="3 months", callback_data="3 months")
      item5 = InlineKeyboardButton(text="Lifetime", callback_data="Lifetime")

      keyboard_inline = InlineKeyboardMarkup().add(item1).add(item2).add(
        item3).add(item4).add(item5)
      text = f"<b> Hii {message.from_user.mention} Select Plan For User <a href='tg://user?id={user_id}'>{username}</a></b>"
      await message.reply(text,
                          reply_markup=keyboard_inline,
                          disable_web_page_preview=True)

    else:

      return await message.reply(
        """<b> <i>You Are Not Allowed To use This Command </i> </b>""",
        disable_web_page_preview=True)

  except Exception as d:
    await message.reply(d)


import time


@dp.message_handler(commands=['deluser'], commands_prefix=PREFIX)
async def infokfc(message: types.Message):

  try:

    query = message.text[len('/deluser '):]
    id = (message.from_user.id)
    if check_admin(id) == True or check_owner(id) == True:
      if len(query) != 0:
        user_id = query
      else:
        try:
          user_id = (message.reply_to_message.from_user.id)
        except:
          return await message.reply("invalid id provided")

      km = await bot.get_chat(user_id)
      username = km.username

      userid = user_id
      delete_specific_UserData(userid)
      return await message.reply(
        f"""<b> Deleted <a href='tg://user?id={user_id}'>{username}</a> </b> From User""",
        disable_web_page_preview=True)
    else:

      return await message.reply(
        """You Are Not Allowed To use This Command """,
        disable_web_page_preview=True)

  except Exception as E:
    await message.reply(E)


@dp.message_handler(commands=['get'], commands_prefix=PREFIX)
async def infokfc(message: types.Message):
  ug = str(message.chat.id)
  user_id = message.from_user.id
  kc = ok(user_id)

  if ug in "-1001603570372":
    if check_admin(user_id) == True:
      await message.reply(
        f'''  {user_id}  <b> Admins You cannot use this command  </b>''')

    alredy = alredyuser()

    if user_id in alredy:
      return await message.reply(
        f'''  {user_id}  <b> is already a preamium </b>''')

    create_user_7days(user_id)
    await message.reply(f"Access granted to 🟩 {message.from_user.username}")

  else:
    await message.reply(f"Access Denied 🟥 {message.from_user.username}")


@dp.message_handler(commands=['tag'], commands_prefix=PREFIX)
async def infokfc(message: types.Message):
  await message.reply("<code>⏤͟͞B3</code>")
