from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils import not_subscribed
import re

@Client.on_message(filters.create(not_subscribed) & filters.text)
async def is_not_subscribed(client, message):
        buttons = [[InlineKeyboardButton(text="ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ", url=client.invitelink)]]
        text = f"sᴏʀʀʏ {message.from_user.mention}\nʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍʏ ʙᴏᴛ."
        await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
