## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCVdHjFKnyzS0qnuuvfeE1f5DvyDv5mwJRA6nUjhgZswWjhA8GI8zWT59WbZ25z1ROJxz4R_Jc41XdfQdLDS4hjPFnU0jS2idcB9HKqC4xqBTTvZDFQz0JwNKeNOJonsrfAftBlzfBbUqI47WetPKeV_ktRaNCY4CwAzD-ZEKnnoXO88EbAokGkKtf5zUtmarEolmdecGhHpDc5cpPg-_TM7PY6VoTi5mIwyn_mNKNqDl92BT_he9IKyS-iLy4uFjGWgZtsODrNXtzIQbGO006jCW7WI1cV1cmJImMYfMWFEfQIuBhVBG-UAF-yzZgRzjT96CNG6NV3Z_rgaJwz4KY_AAAAAUJTS8oA)
BOT_TOKEN = getenv("BOT_TOKEN", "5627838627:AAHOt551a8_ZGixhzcPAIaIkEvwb7-1w-ho)
BOT_NAME = getenv("BOT_NAME", "rody")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "adyqqbot")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ZzZzZ5")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "adyqqbot)
OWNER_ID = getenv("OWNER_ID", "5284259786")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
