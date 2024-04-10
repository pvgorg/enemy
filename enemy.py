from pyrogram import Client, filters
import asyncio
from random import choice

api_id = 16374583
api_hash = "ab378e2c771e0d0d6db66570fe5bbfbc"

app = Client("session_name", api_id, api_hash)

admin_id = 1502490631

fosh_list = []
enemy_list = []

@app.on_message(filters.command("addfosh") & filters.user(admin_id))
async def add_fosh(_, message):
    fosh = message.command[1]
    
    if fosh in fosh_list:
        await message.reply_text(f"**Fosh '{fosh}' already in list.**")
    else:
        fosh_list.append(fosh)
        await message.reply_text(f"**Fosh '{fosh}' added to list.**")
        
@app.on_message(filters.command("delfosh") & filters.user(admin_id))
async def del_fosh(_, message):
    fosh = message.command[1]

    if fosh not in fosh_list:
        await message.reply_text(f"**Fosh '{fosh}' not in list.**")
    else:
        fosh_list.remove(fosh)
        await message.reply_text(f"**Fosh '{fosh}' removed from list.**")
        
@app.on_message(filters.command("clearfosh") & filters.user(admin_id))
async def clear_fosh(_, message):
    fosh_list.clear()
    await message.reply_text("**Fosh list cleared.**")
    
@app.on_message(filters.command("setenemy") & filters.user(admin_id) & filters.reply)
async def set_enemy(_, message):
    replied = message.reply_to_message
    user_id = replied.from_user.id
    
    if user_id in enemy_list:
        await message.reply_text(f"**User {user_id} already an enemy.**") 
    else:
        enemy_list.append(user_id)
        await message.reply_text(f"**User {user_id} added to enemy list.**")
        
@app.on_message(filters.command("delenemy") & filters.user(admin_id) & filters.reply)
async def del_enemy(_, message):
    replied = message.reply_to_message
    user_id = replied.from_user.id

    if user_id not in enemy_list:
        await message.reply_text(f"**User {user_id} not an enemy.**")
    else:
        enemy_list.remove(user_id) 
        await message.reply_text(f"**User {user_id} removed from enemy list.**")
        
@app.on_message(filters.command("clearenemy") & filters.user(admin_id))
async def clear_enemy(_, message):
    enemy_list.clear()
    await message.reply_text("**Enemy list cleared.**")
    
@app.on_message()
async def reply_enemy(_, message):
    if message.from_user.id in enemy_list:
        await message.reply_text(choice(fosh_list))

@app.on_chat_member_updated() 
async def welcome(client, message):
    if message.new_chat_member:
        await message.reply_text("Welcome!")

print("Bot started!")
app.run()
