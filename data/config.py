BOT_TOKEN = '6729042251:AAFOR_MwhaSIjVB7YB8c2ERmtFif_V65xfw'

PREFIX = "!/."

ANTISPAM = int(120)

OWNER = 1226290399

APP_ID = "17428740"

API_HASH = 'c3dc0c1e9e83a7896c9cd60591f3d9b4'

SESSION = ""

OWNERID = int(1226290399)

OWNER_NAME = "<a href='tg://user?id=1226290399'>⏤͟͞B3</a>"

CHANNEL = "https://t.me/Brav_Updates"

GROUP = "https://t.me/Brav_Updates"

OWNER_LINK = "https://t.me/Noir_Tempest_001"

from database import check_user, check_admin

def check_owner(id):
  if id == OWNER: return True
def ok(id):
  if check_owner(id):
    user = "OWNER"
    return user
  if check_admin(id) == True:
    user = "ADMIN"
    return user

  elif check_user(id) == True:
    user = "PAID"
    return user

  elif check_user(id) == False or check_admin(id) == False:
    user = "FREE"
    return user

  else:
    user = "FREE"
    return user
