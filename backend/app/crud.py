from app.database import book_collection
from app.models import Book
from bson import ObjectId

async def create_book(book: Book):
    result = await book_collection.insert_one(book.dict())
    return {"id": str(result.inserted_id)}

async def get_books():
    books = await book_collection.find().to_list(1000)
    return [{"id": str(book["_id"]), **book} for book in books]

async def update_book(book_id: str, book: Book):
    await book_collection.update_one({"_id": ObjectId(book_id)}, {"$set": book.dict()})
    return {"message": "Book updated"}

async def delete_book(book_id: str):
    await book_collection.delete_one({"_id": ObjectId(book_id)})
    return {"message": "Book deleted"}
