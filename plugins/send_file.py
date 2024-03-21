import pyrogram
from pyrogram import filters, Client, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from info import API_ID, API_HASH, BOT_TOKEN, ADMINS, LOG_CHANNEL, DATABASE_NAME, DATABASE_URI, S_GROUP, S_CHANNEL
from Script import script
import time
from utils import temp
from pyrogram.errors import FloodWait
from database.users_db import db
import re
import json
import os
from pyrogram.errors import ChatAdminRequired, FloodWait
import random
import asyncio

@Client.on_message(filters.text & ~filters.command(['start','users','broadcast','stats']))
async def send_series(client, message):
    name = message.text
    name = name.replace("/"," ").replace("."," ").replace(",", " ").replace("''"," ").replace("'"," ").replace("[]"," ").replace("{}"," ").replace("()"," ").replace("`"," ").replace("~"," ").replace("!"," ").replace("@"," ").replace("#"," ").replace("$"," ").replace("%"," ").replace("^"," ").replace("&"," ").replace("*"," ").replace("("," ").replace(")"," ").replace("{"," ").replace("}"," ").replace("["," ").replace("]"," ").replace("-"," ").replace("_"," ").replace("+"," ").replace("="," ")
    name = name.lower()

    if (name == "solo leveling" or name=="solo leveling 2024"):
        buttons = [[
          InlineKeyboardButton('Solo leveling 2024', callback_data='solo_leveling')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo="https://telegra.ph/file/9800929dcf85edbd69133.jpg",
            caption="Title: Solo leveling",
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    else:
        pass

@Client.on_callback_query()
async def callback_handle(client, query):
    if query.data == 'start':
        buttons = [[
            InlineKeyboardButton("🍂 Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀᴛ ", url=f"http://t.me/{temp.U_NAME}?startgroup=true")
            ],[
            InlineKeyboardButton("️🍃 Hᴇʟᴩ", callback_data="help"),
            InlineKeyboardButton("🍁 Aʙᴏᴜᴛ", callback_data="about"),
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.START_TXT.format(query.from_user.mention, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'help':
        buttons = [[
         InlineKeyboardButton('ᴄʜᴇᴄᴋ', callback_data='check'),
         InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.HELP_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'check':
        buttons = [[
         InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help'),
         InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.SERIES_CHECK_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)    

    elif query.data == 'about':
        buttons = buttons = [[
            InlineKeyboardButton("🌿 ʀᴇᴘᴏʀᴛ ʙᴜɢs", callback_data="rrb")
            ],[
            InlineKeyboardButton('Home', callback_data='start'),
            InlineKeyboardButton('close', callback_data='close')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.ABOUT_TXT.format(temp.B_NAME), reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)
        
    elif query.data == 'rrb':
        buttons = [[
            InlineKeyboardButton("🐞 ʀᴇᴘᴏʀᴛ ʙᴜɢs", url=S_GROUP)
            ],[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='about'),
            InlineKeyboardButton('close', callback_data='close')            
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.RRB_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)
        
    elif query.data == 'close':
        await query.message.delete()
        edited_keyboard = InlineKeyboardMarkup([])
        await query.answer()
        await query.message.edit_reply_markup(edited_keyboard)
    elif query.data == 'solo_leveling':
        buttons = [[
            InlineKeyboardButton("season 1", callback_data="solo_seasone")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text="solo leveling_s1_e1-10", reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)
        
    elif query.data == 'solo_seasone':
        buttons = [[
            InlineKeyboardButton("episode 1", callback_data="solo_epi_1"),
            InlineKeyboardButton("episode 2", callback_data="solo_epi_2"),
            InlineKeyboardButton("episode 3", callback_data="solo_epi_3"),
            InlineKeyboardButton("episode 4", callback_data="solo_epi_4")
            ],[
            InlineKeyboardButton("episode 5", callback_data="solo_epi_5"),
            InlineKeyboardButton("episode 6", callback_data="solo_epi_6"),
            InlineKeyboardButton("episode 7", callback_data="solo_epi_7"),
            InlineKeyboardButton("episode 8", callback_data="solo_epi_8")
            ],[
            InlineKeyboardButton("episode 9", callback_data="solo_epi_9"),
            InlineKeyboardButton("episode 10", callback_data="solo_epi_10"),
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text="solo leveling s1 e1-10", reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'solo_epi_1':
        user_id = query.from_user.id
        await client.send_document(user_id,"BQACAgQAAxkBAAMeZfxPpdlbuRgrJMpNcRGpEuYAAVm1AAJFEQACfxHgUOhCxmEDyOpqHgQ")
          
    elif query.data == 'solo_epi_2':
        user_id = query.from_user.id 
        await client.send_document(user_id,"BQACAgQAAxkBAAMgZfxTEs1TzQRgvnrT8-48NpVqhzsAAmQSAAK1eBlRdB2soOtgpBgeBA")

    elif query.data == 'solo_epi_3':
        user_id = query.from_user.id   
        await client.send_document(user_id,"BQACAgQAAxkBAAMiZfxTI5OSpkjBPMyHp1F5Iu-lp68AAkkSAAIBjWBR1tvEDjNCeC8eBA")
          
    elif query.data == 'solo_epi_4':
        user_id = query.from_user.id  
        await client.send_document(user_id,"BQACAgQAAxkBAAMkZfxTLXKk1S_gZB_agDSSrhvQBEcAApcUAALka6hRDc6CLe_1GdEeBA")      

    elif query.data == 'solo_epi_5':
        user_id = query.from_user.id
        await client.send_document(user_id,"BQACAgQAAxkBAAMmZfxTOUa5oneBkqrmC3QHXOi-lsoAAvoTAALUafhR8Z9cx1d6MG8eBA")
          
    elif query.data == 'solo_epi_6':
        user_id = query.from_user.id 
        await client.send_document(user_id,"BQACAgQAAxkBAAMoZfxTRT8cRRYCCCF8GgKGpvNX0lIAAiYSAAKfwkBS5vhn5yY2Bt8eBA")

    elif query.data == 'solo_epi_7':
        user_id = query.from_user.id 
        await client.send_document(user_id,"BQACAgQAAxkBAAMqZfxTTmBJf5TF5aDbAmsj7VObfa8AAhwSAAKVOYhSd8rCjBsll98eBA")
          
    elif query.data == 'solo_epi_8':
        user_id = query.from_user.id  
        await client.send_document(user_id,"BQACAgQAAxkBAAMsZfxTWYFmcvmhX-Eu_zbuC4JDzGMAAt0SAAIxQCBTqO-zrtoZde4eBA")           
      
    elif query.data == 'solo_epi_9':
        user_id = query.from_user.id
        await client.send_document(user_id,"BQACAgQAAxkBAAMuZfxTZFIORGsxNMK_EaflUUfnlecAAhERAAKr_2FTnyGryxdqCUAeBA")
  
    elif query.data == 'solo_epi_10':
        user_id = query.from_user.id
        await client.send_document(user_id,"BQACAgQAAxkBAAMwZfxTcK2BI-YCT3DP-gABQh2s4J89AALDEAACIe65U8gMsXEoxOI6HgQ")                   
