from pyrogram import Client, filters, enums
from pyrogram.types import Message, ChatPermissions
from datetime import datetime
import os
import time
import psutil
import random
from os import environ
import asyncio

def format_uptime(seconds):
    days = seconds // (24*60*60)
    seconds %= (24*60*60)
    hours = seconds // (60*60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    return f"{days} ᴅᴀʏs, {hours} ʜᴏᴜʀs, {minutes} ᴍɪɴᴜᴛᴇs"

# help message

@user.on_message(filters.command("help",prefixes="."))
async def help_handler(client: user, message: Message):
    help_text = f"ʜᴇʏ {message.from_user.mention}\n\n ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ʜᴏᴡ ᴛᴏ ᴜsᴇ\n\n<code>.alive</code> = Check the userbot is alive or not\n<code>.help</code> = show the full command and description\n<code>.uptime</code> = The measure of how long a bot is on and available.\n<code>.ping</code>\n<code>.approve</code> = Approve all pending join requests in a chat.\n<code>.promote</code> = Promote chat member to admin and Set a custom title (rank) to an administrator of a supergroup.(Eg:- .promote co-admin)\n<code>.mute</code> = mute a user in a group.\n<code>.unmute</code>= unmute a user in a group \n<code>.pin</code> = Pin a message in a group\n<code>.upin</code> = UnPin a message in a group\n<code>.unpin_all</code> = UnPin all message in a group\n<code>.group_close</code> = Only group admin can send messages\n<code>.group_open</code> = Everyone can send message\n<code>.new_profile</code> = First resize photo to sqare shape and then send the command to reply the photo\n<code>.leave</code> = You can leave from a group or channel using .leave command\n<code>.string</code>\n<code>.id</code> = to get the user id\n<code>.set_pic</code> = Set a new photo for group"
    await message.reply_text(help_text)

# uptime

@user.on_message(filters.command("uptime", prefixes="."))
async def uptime_handler(client: user, message: Message):
    uptime = format_uptime(time.time() - psutil.boot_time())
    await client.send_message(message.chat.id, text=f"{uptime}")

#alive message

@user.on_message(filters.command("alive", prefixes="."))
async def alive_handler(client: user, message: Message):
    await client.send_photo(message.chat.id, "https://telegra.ph/file/683258036c3245d6ee95e.jpg", caption=f"ʜɪ {message.from_user.mention},\nɪ ᴀᴍ ᴀʟɪᴠᴇ,ᴅᴏɴ'ᴛ ʙᴇ sᴄᴀᴍ")

#ping

@user.on_message(filters.command("ping", prefixes="."))
async def ping_handler(client: user, message: Message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"<b>🏓 Pong!\n<code>{time_taken_s:.3f} ms</code>\n</b>")

#pending approve in group/channel

@user.on_message(filters.command("approve",prefixes=".") & ~filters.private)
async def approve_handler(client: user, message: Message):
  try:
    id = message.chat.id
    await client.approve_all_chat_join_requests(id)
    await message.reply_text("all completed")
  except Exception as e:
    await message.reply_text(f"{e}")

# promote to admin and adding the title(only admins can use this command)

@user.on_message(filters.command("promote", prefixes=".") & filters.group)
async def promote_handler(client: user, message: Message):
    try:
     msg = message.text.split()[1::]
     msg = " ".join(msg)
     if len(msg)>0:
        user_id = message.reply_to_message.from_user.id
        user = await client.get_chat_member(message.chat.id , message.from_user.id)
        if user.status not in [enums.ChatMemberStatus.OWNER , enums.ChatMemberStatus.ADMINISTRATOR]:
           raise PermissionError("You are not allowed to use this command")
        await client.promote_chat_member(message.chat.id, user_id)
        await client.set_administrator_title(message.chat.id, user_id, f"{msg}")
        i=await message.reply_text("Completed")
        await asyncio.sleep(20)
        await i.delete()
     else:
        user_id = message.reply_to_message.from_user.id
        user = await client.get_chat_member(message.chat.id , message.from_user.id)
        if user.status not in [enums.ChatMemberStatus.OWNER , enums.ChatMemberStatus.ADMINISTRATOR]:
           raise PermissionError("You are not allowed to use this command")
        await client.promote_chat_member(message.chat.id , user_id)
        h=await message.reply_text("Completed")
        await asyncio.sleep(20)
        await h.delete()
    except Exception as e:
        await message.reply_text(f"{e}")

# mute a user in the group(only admins can use this command)

@user.on_message(filters.command("mute",prefixes=".") & filters.group)
async def mute_handler(client: user, message:Message):
   try:
        user_id = message.reply_to_message.from_user.id
        user = await client.get_chat_member(message.chat.id , message.from_user.id)
        if user.status not in [enums.ChatMemberStatus.OWNER , enums.ChatMemberStatus.ADMINISTRATOR]:
           raise PermissionError("You are not allowed to use this command")
        await client.restrict_chat_member(message.chat.id , user_id , ChatPermissions(
            can_send_messages=False ,
            can_send_media_messages=False ,
            can_send_other_messages=False ,
            can_send_polls=False ,
            can_add_web_page_previews=False ,
            can_change_info=False ,
            can_invite_users=False ,
            can_pin_messages=False
        ))
        await message.reply_text("successfully muted")
   except Exception as e:
        await message.reply_text(f"{e}")

#unmute the muted user in the group(only admins can use this command)

@user.on_message(filters.command("unmute",prefixes=".") & filters.group)
async def unmute_handler(client: user, message:Message):
   try:
        user_id = message.reply_to_message.from_user.id
        user = await client.get_chat_member(message.chat.id , message.from_user.id)
        if user.status not in [enums.ChatMemberStatus.OWNER , enums.ChatMemberStatus.ADMINISTRATOR]:
           raise PermissionError("You are not allowed to use this command")
        await client.restrict_chat_member(message.chat.id , user_id , ChatPermissions(
            can_send_messages=True ,
            can_send_media_messages=True ,
            can_send_other_messages=True ,
            can_send_polls=True ,
            can_add_web_page_previews=True ,
            can_change_info=True ,
            can_invite_users=True ,
            can_pin_messages=True
        ))
        await message.reply_text("successfully unmuted")
   except Exception as e:
        await message.reply_text(f"{e}")

# pin a message(only admins can use this command)

@user.on_message(filters.command("pin",prefixes=".") & filters.group)
async def pin_handler(client: user, message: Message):
    try:
     msg = message.reply_to_message_id
     user = await client.get_chat_member(message.chat.id , message.from_user.id)
     if user.status not in [enums.ChatMemberStatus.OWNER , enums.ChatMemberStatus.ADMINISTRATOR]:
         raise PermissionError("You are not allowed to use this command")
     await client.pin_chat_message(message.chat.id, msg)
    except Exception as e:
     await message.reply_text(f"{e}")

# unpin the pinned message(only admins can use this command)

@user.on_message(filters.command("unpin",prefixes=".") & filters.group)
async def unpin_handler(client: user, message: Message):
    try:
     msg = message.reply_to_message_id
     user = await client.get_chat_member(message.chat.id , message.from_user.id)
     if user.status not in [enums.ChatMemberStatus.OWNER , enums.ChatMemberStatus.ADMINISTRATOR]:
         raise PermissionError("You are not allowed to use this command")
     await client.unpin_chat_message(message.chat.id, msg)
    except Exception as e:
     await message.reply_text(f"{e}")

# unpin all the pinned message(only admins can use this command)

@user.on_message(filters.command("unpin_all",prefixes=".") & filters.group)
async def unpinall_handler(client: user, message: Message):
    try:
     user = await client.get_chat_member(message.chat.id , message.from_user.id)
     if user.status not in [enums.ChatMemberStatus.OWNER , enums.ChatMemberStatus.ADMINISTRATOR]:
         raise PermissionError("You are not allowed to use this command")
     await client.unpin_all_chat_messages(message.chat.id)
    except Exception as e:
     await message.reply_text(f"{e}")

# group close(only admins can use this command)

@user.on_message(filters.command("group_close",prefixes=".") & filters.group)
async def group_close_handler(client: user, message: Message):
    user = await client.get_chat_member(message.chat.id , message.from_user.id)
    if user.status not in [enums.ChatMemberStatus.OWNER , enums.ChatMemberStatus.ADMINISTRATOR]:
        raise PermissionError("You are not allowed to use this command")
    await client.set_chat_permissions(message.chat.id, ChatPermissions(
        can_send_messages=False ,
        can_send_media_messages=False ,
        can_send_other_messages=False ,
        can_send_polls=False ,
        can_add_web_page_previews=False ,
        can_change_info=False ,
        can_invite_users=False ,
        can_pin_messages=False
    ))
    await message.reply_text("This group is closed")

# group open(only admins can use this command)

@user.on_message(filters.command("group_open",prefixes=".") & filters.group)
async def group_open_handler(client: user, message: Message):
    user = await client.get_chat_member(message.chat.id , message.from_user.id)
    if user.status not in [enums.ChatMemberStatus.OWNER , enums.ChatMemberStatus.ADMINISTRATOR]:
        raise PermissionError("You are not allowed to use this command")
    await client.set_chat_permissions(message.chat.id, ChatPermissions(
        can_send_messages=True ,
        can_send_media_messages=True ,
        can_send_other_messages=True ,
        can_send_polls=True ,
        can_add_web_page_previews=True ,
        can_change_info=True ,
        can_invite_users=True ,
        can_pin_messages=True
    ))
    await message.reply_text("This group is opened")

# adding new profile for ur account(only can use it)

@user.on_message(filters.command("new_profile", prefixes=".") & filters.me)
async def new_pic_handler(client: user, message: Message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        return await message.reply_text("Reply to a photo or video to set the profile picture.")

    photo_path = await message.reply_to_message.download()
    try:
        await client.set_profile_photo(photo=photo_path)
        await message.reply_text("Profile picture set!")
    except Exception as e:
        await message.reply_text(f"Error setting profile picture: {e}")
    finally:
        os.remove(photo_path)

# leave from a chat/channel(only can use it)

@user.on_message(filters.command("leave",prefixes=".") & filters.me)
async def leave_handler(client: user, message: Message):
    id = message.chat.id
    group_name = message.chat.title
    await client.leave_chat(id)
    await client.send_message("me", text=f"Leaved from {group_name} successful")

# get the user id(everyone can use it)

@user.on_message(filters.command("id",prefixes="."))
async def id_handler(client:user, message:Message):
      chat_type = message.chat.type
      if chat_type in [enums.ChatType.PRIVATE]:
        user_id = message.from_user.id
        first = message.from_user.first_name
        last = message.from_user.last_name or ""
        username = message.from_user.username
        dc_id = message.from_user.dc_id or ""
        fake = message.from_user.is_fake
        bot = message.from_user.is_bot
        scam = message.from_user.is_scam
        upgrade = message.from_user.is_premium
        verify = message.from_user.is_verified
        online = message.from_user.last_online_date or ""
        await message.reply_text(f"<b>➲ ғɪʀsᴛ ɴᴀᴍᴇ:</b> {first}\n<b>➲ ʟᴀsᴛ ɴᴀᴍᴇ:</b> {last}\n<b>➲ ᴜsᴇʀɴᴀᴍᴇ:</b> @{username}\n<b>➲ ɪᴅ:</b> <code>{user_id}</code>\n<b>➲ ᴅᴄ ɪᴅ:</b> <code>{dc_id}</code>\n➲ Is ғᴀᴋᴇ: {fake}\n➲ Is ʙᴏᴛ: {bot}\n➲ ɪs sᴄᴀᴍ: {scam}\n➲ Is ᴠᴇʀɪғɪᴇᴅ: {verify}\n➲ Is ᴘʀᴇᴍɪɴᴜᴍ: {upgrade}\n➲ Lᴀsᴛ ᴏɴʟɪɴᴇ ᴅᴀᴛᴇ: {online}", quote=True)
      elif chat_type in [enums.ChatType.GROUP , enums.ChatType.SUPERGROUP]:
          if message.reply_to_message:
              user_id = message.reply_to_message.from_user.id
              first = message.reply_to_message.from_user.first_name
              last = message.reply_to_message.from_user.last_name or ""
              username = message.reply_to_message.from_user.username
              dc_id = message.reply_to_message.from_user.dc_id or ""
              fake = message.reply_to_message.from_user.is_fake
              bot = message.reply_to_message.from_user.is_bot
              scam = message.reply_to_message.from_user.is_scam
              upgrade = message.reply_to_message.from_user.is_premium
              verify = message.reply_to_message.from_user.is_verified
              online = message.reply_to_message.from_user.last_online_date or ""
              await message.reply_text(
                  f"<b>➲ ғɪʀsᴛ ɴᴀᴍᴇ:</b> {first}\n<b>➲ ʟᴀsᴛ ɴᴀᴍᴇ:</b> {last}\n<b>➲ ᴜsᴇʀɴᴀᴍᴇ:</b> @{username}\n<b>➲ ɪᴅ:</b> <code>{user_id}</code>\n<b>➲ ᴅᴄ ɪᴅ:</b> <code>{dc_id}</code>\n➲ Is ғᴀᴋᴇ: {fake}\n➲ Is ʙᴏᴛ: {bot}\n➲ ɪs sᴄᴀᴍ: {scam}\n➲ Is ᴠᴇʀɪғɪᴇᴅ: {verify}\n➲ Is ᴘʀᴇᴍɪɴᴜᴍ: {upgrade}\n➲ Lᴀsᴛ ᴏɴʟɪɴᴇ ᴅᴀᴛᴇ: {online}" ,
                  quote=True)
          else:
            grp_id = message.chat.id
            first = message.chat.title
            await message.reply_text(
                f"<b>➲ ɢʀᴏᴜᴘ ɴᴀᴍᴇ:</b> {first}\n<b>➲ ɢʀᴏᴜᴘ ɪᴅ:</b> {grp_id}\n" ,
                quote=True)

# set profile pic for chat(only group admins can do it).

@user.on_message(filters.command("set_pic",prefixes=".") & filters.group)
async def set_pic_handler(client: user, message: Message):
    user = await client.get_chat_member(message.chat.id , message.from_user.id)
    if user.status not in [enums.ChatMemberStatus.OWNER , enums.ChatMemberStatus.ADMINISTRATOR]:
        raise PermissionError("You are not allowed to use this command")
    if message.reply_to_message.photo:
         pic = message.reply_to_message.photo.file_id
         await client.set_chat_photo(message.chat.id, photo=pic)
         await message.reply_text(f"New profile photo has been set for this group")
    elif not message.reply_to_message.photo:
        await message.reply_text("please reply to photo")

# if anyone mentioned in a group it will automatically send message.

@user.on_message(filters.group)
async def mention_handler(client: user, message: Message):
    if message.text is None:
        return
    elif message.text == "@MrTG_Coder":
        await message.reply_text("Unfortunately, @MrTG_Coder is currently unavailable. They will respond as soon as they are online.")
    elif "@MrTG_Coder" in message.text:
        await message.reply_text(
            f"Unfortunately, @MrTG_Coder is currently unavailable. They will respond as soon as they are online.")
    else:
        pass
