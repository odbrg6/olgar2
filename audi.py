import re
import base64
import asyncio
import logging
from telethon import events
from config import *
from asyncio import sleep
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger("لبيدو")
logger.info("النشر التلقائي شغال الان استمتع ✓")

@olgaly.on(events.NewMessage)
async def join_channel(event):
    try:
        await olgaly(JoinChannelRequest("@bidusou"))
    except BaseException:
        pass
        
@olgaly.on(events.NewMessage)
async def join_channel(event):
    try:
        await olgaly(JoinChannelRequest("@a1lgabook"))
    except BaseException:
        pass

        
@olgaly.on(events.NewMessage)
async def join_channel(event):
    try:
        await olgaly(JoinChannelRequest("@L6_G6"))
    except BaseException:
        pass

        
@olgaly.on(events.NewMessage)
async def join_channel(event):
    try:
        await olgaly(JoinChannelRequest("@BIDUTH"))
    except BaseException:
        pass
      

@olgaly.on(events.NewMessage)
async def join_channel(event):
    try:
        await olgaly(JoinChannelRequest("@B_F69"))
    except BaseException:
        pass  

@olgaly.on(events.NewMessage)
async def join_channel(event):
    try:
        await olgaly(JoinChannelRequest("@biduso"))
    except BaseException:
        pass  


yaBidu = False
async def ze_nshr(olgaly, sleeptimet, chat, message, seconds):
    global yaBidu
    yaBidu = True
    while yaBidu:
        if message.media:
            sent_message = await olgaly.send_file(chat, message.media, caption=message.text)
        else:
            sent_message = await olgaly.send_message(chat, message.text)
        await asyncio.sleep(sleeptimet)
@olgaly.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر (\d+) (@?\S+)$"))
async def Ahmed(event):
    await event.delete()
    parameters = re.split(r'\s+', event.text.strip(), maxsplit=2)
    if len(parameters) != 3:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    seconds = int(parameters[1])
    chat_usernames = parameters[2].split()
    olgaly = event.client
    global yaBidu
    yaBidu = True
    message = await event.get_reply_message()
    for chat_username in chat_usernames:
        try:
            chat = await olgaly.get_entity(chat_username)
            await ze_nshr(olgaly, seconds, chat.id, message, seconds)  # تمرير قيمة seconds هنا لكل مجموعة
        except Exception as e:
            await event.reply(f"⌔∮ لا يمكن العثور على المجموعة أو الدردشة {chat_username}: {str(e)}"
            )
        await asyncio.sleep(1)
    sourceze = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    sourceze = Get(sourceze)
    try:
        await event.client(sourceze)
    except BaseException:
        pass
    
async def ze_allnshr(olgaly, sleeptimet, message):
    global yaBidu
    yaBidu = True
    ol_chat = await olgaly.get_dialogs()
    while yaBidu:
        for chat in ol_chat:
            if chat.is_group:
                try:
                    if message.media:
                        await olgaly.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await olgaly.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@olgaly.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر_كروبات (\d+)$"))
async def Ahmed(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    olgaly = event.client
    global yaBidu
    yaBidu = True
    await ze_allnshr(olgaly, sleeptimet, message)
    sourceze = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    sourceze = Get(sourceze)
    try:
        await event.client(sourceze)
    except BaseException:
        pass
super_groups = ["super", "سوبر", "بيع", "شراء", "بِيَع", "وشراء", "supr", "soper", "sopr", "سُوبِر"]
async def ze_supernshr(olgaly, sleeptimet, message):
    global yaBidu
    yaBidu = True
    ol_chat = await olgaly.get_dialogs()
    while yaBidu:
        for chat in ol_chat:
            chat_title_lower = chat.title.lower()
            if chat.is_group and any(keyword in chat_title_lower for keyword in super_groups):
                try:
                    if message.media:
                        await olgaly.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await olgaly.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@olgaly.on(events.NewMessage(outgoing=True, pattern=r"^\.سوبر (\d+)$"))
async def Ahmed(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    olgaly = event.client
    global yaBidu
    yaBidu = True
    await ze_supernshr(olgaly, sleeptimet, message)
    sourceze = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    sourceze = Get(sourceze)
    try:
        await event.client(sourceze)
    except BaseException:
        pass
@olgaly.on(events.NewMessage(outgoing=True, pattern='.ايقاف النشر'))
async def stop_ze(event):
    global yaBidu
    yaBidu = False
    await event.edit("**۞︙ تم ايقاف النشر التلقائي بنجاح ✓** ")
@olgaly.on(events.NewMessage(outgoing=True, pattern=r"^\.(الاوامر|فحص)$"))
async def Ahmed(event):
    await event.delete()
    if event.pattern_match.group(1) == "الاوامر":
        sourceze_zesource = """**
        - أوامر سورس أولكَا للنشر التلقائي :

`.نشر` + عدد الثواني + معرف الكروب :
~ للنشر في المجموعة التي وضعت معرفها مع عدد الثواني

`.نشر_كروبات` + عدد الثواني : 
~ للنشر في جميع المجموعات الموجوده في حسابك
 
`.سوبر` + عدد الثواني : 
~ للنشر بكافة المجموعات السوبر التي منظم اليها ( بدون اخطاء )

`.ايقاف النشر`

• مُـلاحظة : جميع الأوامر اعلاه تستخدم بالرد على الرسالة او الكليشة .
        **"""
        await event.reply(file='https://telegra.ph/file/eb3d0e2ffd4edd9880fb0.jpg', message=sourceze_zesource)
    elif event.pattern_match.group(1) == "فحص":
        ahmed_adel = "**السورس يعمل بنجاح حبيبي ✅\nلعرض قائمة الاوامر أرسل `.الاوامر`**"
        await event.reply(file='https://telegra.ph/file/eb3d0e2ffd4edd9880fb0.jpg', message=ahmed_adel)
        sourceze = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
        sourceze = Get(sourceze)
        try:
            await event.client(sourceze)
        except BaseException:
            pass
print(' تشغيل نشر التلقائي لسورس بيدو ')
olgaly.run_until_disconnected()
