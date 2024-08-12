from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "24574525")
APP_HASH = os.environ.get("APP_HASH", "d9c4c2459f68da63c58517e431d49149")
SESSION = os.environ.get("TERMUX", "1ApWapzMBu8Oow6xKmz7ZZq5QNGXpjD2g8t_LzTSs3Xl2Hiu6MwuoOUeWjJQPI5NOrtR8C9NvEUV34PYJVwFxvNrcB03xBYRT_rbw2VwCWx-2CAIB7BJ7RSLGg55olIlM1m3EZCAwDc8jB5fn-HVuJg0s0yOQwBKnzcuPavAQFuqXtd82tZCyEsw5PE2Sd0ATEPA1yvsunuyug2uXT9fgLIDjmV6d9IDjmbondwY3uDhPWuECRNXIqUOY2VdnN92PWC2GnblaTI7kKmSCRwWHEuJsB8LLucFpK8b7o7ZgfPKSeMR1bZeMRsJJP5fud_L6ATJDigtlvrVTS1djVGGF1uqE3JjqCtQ=")
olgaly = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
olgaly.start()
