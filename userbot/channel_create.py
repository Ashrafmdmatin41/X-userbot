import asyncio
import re
import os
from os import environ
from pyrogram import enums, Client as user, filters
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://sakurabis11:woljkA2QEGi03iYY@cluster0.w1oavmr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Adjust for your MongoDB setup

mongo_client = MongoClient(MONGO_URI)
db = mongo_client["sakurabis11"]  
channel_collection = db["Telegram_files"]  


async def ensure_channel_exists():
    """
    Checks for and creates a channel if necessary, storing the ID in MongoDB.
    """
    existing_channel = channel_collection.find_one()
    if existing_channel:
        return existing_channel["channel_id"]
    else:
        try:
            await client.create_channel("my user bot")
            chat = await client.create_channel("my user bot")
            channel_id = chat.id
            await channel_collection.insert_one({"channel_id": channel_id})
            return channel_id
        except Exception as e:
            print(f"Error creating channel: {e}")
            return None


@user.on_message(filters.command("start"))
async def start_handler(client: user, message):
    channel_id = await ensure_channel_exists()
    if channel_id:
        await message.reply_text(f"Channel already exists: {channel_id}")
    else:
        await message.reply_text("Failed to create channel. Please check logs for details.")
