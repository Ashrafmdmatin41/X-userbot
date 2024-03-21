import os
from pyrogram.errors import ChatAdminRequired, FloodWait
import random
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import enums, filters, Client
from info import API_ID, API_HASH, BOT_TOKEN, ADMINS, LOG_CHANNEL, DATABASE_NAME, DATABASE_URI, S_GROUP, S_CHANNEL
from Script import script
import time
from utils import temp
from pyrogram.errors import FloodWait
from database.users_db import db
import re
import json
import base64
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        buttons = [[
            InlineKeyboardButton("ʜᴇʟᴘ", url=f"https://t.me/{temp.U_NAME}?start=help"),
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(text=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup)
        await asyncio.sleep(2)
        if not await db.get_chat(message.chat.id):
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, "Unknown"))       
            await db.add_chat(message.chat.id, message.chat.title)
        return await message.reply(script.START_TXT.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup)
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention, message.from_user.id))
    if len(message.command) != 2:
        buttons = [[
            InlineKeyboardButton("️🍃 Hᴇʟᴩ", callback_data="help"),
            InlineKeyboardButton("🍁 Aʙᴏᴜᴛ", callback_data="about")
            ],[
            InlineKeyboardButton("🌿 ᴄʟᴏsᴇ", callback_data='close')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(text=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup)

