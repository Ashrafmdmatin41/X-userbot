import motor.motor_asyncio
from info import DATABASE_NAME, DATABASE_URI

class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users
        self.grp = self.db.groups
        self.chnl = self.db.channels

    async def add_channel(self, chat, title):
        chat = self.new_channel(chat, title)
        await self.chnl.insert_one(chat)

db = Database(DATABASE_URI, DATABASE_NAME)
