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
from pyrogram.raw.all import layer
from pyrogram import types
import aiohttp


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
        logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")

        logger.info("Running...")
        print(f"{me.first_name} | @{me.username} started...")


if __name__ == "__main__":
   app = Bot()
   app.run()
