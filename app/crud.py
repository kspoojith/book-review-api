from app.database import book_collection

async def add_book(book: dict):
    await book_collection.insert_one(book)
    return book

async def get_books():
    return [doc async for doc in book_collection.find()]

async def get_book(title: str):
    return await book_collection.find_one({"title": title})

async def update_book(title: str, data: dict):
    await book_collection.update_one({"title": title}, {"$set": data})

async def delete_book(title: str):
    await book_collection.delete_one({"title": title})
