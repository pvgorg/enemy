from telethon import TelegramClient , events
from os import listdir as L
from json import load,dump
from random import choice as C

api_id = 12701321 # آی پی آی آیدی بزارید
api_hash = "83995b97cd109d02c1ead50c9f6f5605" # آی پی آی هش بزارید
with TelegramClient('sjsjbsbs', api_id, api_hash) as client:
   client.send_message('me', '✅ با موفقیت سلف روی اکانت شما ران شد میتوانید با ارسال پیام\n`Help`\nکامند های ربات رو دریافت کنید با تشکر سازنده ربات آراز\n\n🆔 @roh_bijan')
   print(client.download_profile_photo('me'))

AdminBot = 1502490631 #ایدی عددی ادمین

foshall_list = []


@client.on(events.NewMessage(pattern=r"AddFosh (.*)" , from_users=AdminBot))
async def add_name(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    xxx = (input_str)
    if (xxx) in foshall_list:
        await event.edit(f"**Fosh ( {xxx} ) In Fosh Listed . . . !**")
    else:
        try:
            foshall_list.append(xxx)
            await event.edit(f"**Fosh ( {xxx} ) Added In Fosh List . . . !**")
        except:
            await event.edit("**No Invalid . . . !**")

@client.on(events.NewMessage(pattern=r"DelFosh (.*)" , from_users=AdminBot))
async def del_name(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    xxx = (input_str)
    if (xxx) not in foshall_list:
        await event.edit(f"**Fosh ( {xxx} ) Not In Fosh Listed . . . !**")
    else:
        try:
            foshall_list.remove(xxx)
            await event.edit(f"**Fosh ( {xxx} ) Removed In Fosh List . . . !**")
        except:
            await event.edit("**No Invalid . . . !**")

@client.on(events.NewMessage())
async def clean_name(event):
    text = (event.raw_text)
    if (text == "ClearFosh" and event.sender_id == AdminBot):
        if foshall_list == []:
            await event.edit("**Fosh List Has Been Empty . . . !**")
        else:
            foshall_list.clear()
            await event.edit("**Fosh List Has Been Cleared . . . !**")
            
        
@client.on(events.ChatAction)
async def leftMember(event):
    if event.user_joined:
        await event.reply("Welcome To The Group !\nMy Self Creator : @roh_bijan")

@client.on(events.NewMessage())
async def timebio_on(event):
    text = (event.raw_text)
    if (text == "Help" and event.sender_id == AdminBot):
        await event.edit("**Welcome To Enemy Help !\n\nتوجه : \nبرای افزودن دشمن حداقل باید یک عدد فحش اضافه کنید نکنید چیزی نمیگه میتونید بجای فحش قلب هم اضافه کنی بجای فحش قلب بده در آینده آپدیت میشود هم قلب دار هم دشمن اضافه میشود!\n\n برای افزودن دشمن (هر پیامی بده ریپلای میکنه فحش میده) : \n `SetEnemy` (Reply)\n برای در آوردن از قسمت دشمن : \n `DelEnemy` (Reply) \nبرای پاک کردن کل دشمنان : \n `ClearEnemy`\nتنظیم کردن فحش جدید : \n `AddFosh` (Text) \n برای پاک کردن فحش : \n `DelFosh` (Text) \n برای پاک کردن کل لیست فحش : \n `ClearFosh`\n\nDeveloper : @roh_bijan**")
        
@client.on(events.NewMessage(from_users=AdminBot))
async def _(event):
    if event.raw_text.lower() == "setenemy":
        chat = await event.get_chat()
        replied = await event.get_reply_message()
        sender = replied.sender
        xxx = int("{}".format(sender.id))
        if int(xxx) in enemyall_list:
            await event.edit("**User Has Already Enemy !**".format(sender.first_name , sender.id))
        else:
            try:
                enemyall_list.append(int(xxx))
                await event.edit("**User Has Enemy Seted**".format(sender.first_name , sender.id))
            except:
                await event.edit("**No Invalid . . . !**")
    elif event.raw_text.lower() == "delenemy":
        chat = await event.get_chat()
        replied = await event.get_reply_message()
        sender = replied.sender
        xxx = int("{}".format(sender.id))
        if int(xxx) not in enemyall_list:
            await event.edit("**User Has Not Enemy**".format(sender.first_name , sender.id))
        else:
            try:
                enemyall_list.remove(int(xxx))
                await event.edit("**User Has Delete Enemy**".format(sender.first_name , sender.id))
            except:
                await event.edit("**No Invalid . . . !**")
@client.on(events.NewMessage())
async def clean_name(event):
    text = (event.raw_text)
    if (text == "ClearEnemy" and event.sender_id == AdminBot):
        if enemyall_list == []:
            await event.edit("**Enemy List Has Been Empty . . . !**")
        else:
            enemyall_list.clear()
            await event.edit("**Enemy List Has Been Cleared . . . !**")
                

@client.on(events.NewMessage)
async def enemy(event):
    if event.sender_id in enemyall_list:
        await event.reply(C(foshall_list))
                
        
        
        
client.start()
client.run_until_disconnected()
asyncio.get_event_loop().run_forever()
#کسننت منبع بپاکی یا اسکی بری
