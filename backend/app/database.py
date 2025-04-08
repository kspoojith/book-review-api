import motor.motor_asyncio
from os import getenv

MONGO_DETAILS = getenv("MONGO_DETAILS", "mongodb://localhost:27017")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.bookstore
book_collection = database.get_collection("books")
