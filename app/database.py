import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = f"mongodb://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASS')}@{os.getenv('MONGO_HOST')}:{os.getenv('MONGO_PORT')}"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client[os.getenv('MONGO_DB')]
book_collection = database.get_collection("books")
