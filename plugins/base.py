from pyrogram import Client, filters, enums
from info import ADMINS
from database.users_db import db
from utils import get_size, temp
from Script import script
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong, PeerIdInvalid

@Client.on_message(filters.command('users') & filters.user(ADMINS))
async def list_users(bot, message):
    # https://t.me/GetTGLink/4184
    raju = await message.reply('Getting List Of Users')
    users = await db.get_all_users()
    out = "Users Saved In DB Are:\n\n"
    async for user in users:
        out += f"<a href=tg://user?id={user['id']}>{user['name']}</a>"
        if user['ban_status']['is_banned']:
            out += '( Banned User )'
        out += '\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('users.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('users.txt', caption="List Of Users")

@Client.on_message(filters.command('stats'))
async def get_stats(bot, message):
    rju = await message.reply('Fetching stats..')
    total_users = await db.total_users_count()
    total_chats = await db.total_chat_count()
    size = await db.get_db_size()
    free = 536870912 - size
    size = get_size(size)
    free = get_size(free)    
    await rju.edit(script.STATUS_TXT.format(total_users, total_chats))
