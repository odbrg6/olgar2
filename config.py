from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "24574525")
APP_HASH = os.environ.get("APP_HASH", "d9c4c2459f68da63c58517e431d49149")
SESSION = os.environ.get("TERMUX")
olgaly = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
olgaly.start()