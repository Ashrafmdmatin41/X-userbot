from pyrogram import Client, __version__, filters
from info import API_ID, API_HASH, SESSION
import os, math, logging, pytz
from datetime import date, datetime 
from pytz import timezone
import logging.config
from pyrogram.errors import BadRequest, Unauthorized
from typing import Union, Optional, AsyncGenerator
import pytz
import aiohttp
import motor.motor_asyncio
import pymongo
from pymongo import MongoClient
from pyrogram.errors import ChatForbidden
from pyrogram.raw.all import layer
from pyrogram import types
import aiohttp
from info import DATABASE_COLLECTION, DATABASE_NAME, DATABASE_URI

logging.config.fileConfig("logging.conf")
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="user-bot",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION,
            workers=50,
            plugins={"root": "userbot"},
            sleep_threshold=5,
        )
    async def start(self):
        await super().start()
        logging.info(f"for Pyrogram v{__version__} (Layer {layer}) started.")

        logger.info("Running...")
        print(f"started...")
        supergroup_id = None
        if supergroup_id not in DATABASE_COLLECTION.find_one("id"):
           print("Supper group is creating started")
           supergroup = await client.create_supergroup(f"{message.from_user.first_name} X-Userbot")
           supergroup_id = supergroup.id
           DATABASE_COLLECTION.insert_one({"id": supergroup_id})
           await client.send_message(supergroup_id, text="SuperGroup creation completed")
        elif supergroup_id in DATABASE_COLLECTION.find_one("id"):
           pass

           
        



if __name__ == "__main__":
   app = Bot()
   app.run()
