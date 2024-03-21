import pyrogram
from pyrogram import Client, filters
from info import ADMINS

@Client.on_message(filters.document & filters.private & filters.user(ADMINS))
async def fileid(client, message):
   await message.reply(message.document.file_id)
