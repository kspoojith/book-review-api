from fastapi import FastAPI, HTTPException
from app.models import Book
from app.crud import add_book, get_books, get_book, update_book, delete_book

app = FastAPI()

@app.post("/books")
async def create_book(book: Book):
    return await add_book(book.dict())

@app.get("/books")
async def read_books():
    return await get_books()

@app.get("/books/{title}")
async def read_book(title: str):
    book = await get_book(title)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{title}")
async def modify_book(title: str, book: Book):
    await update_book(title, book.dict())
    return {"message": "Book updated"}

@app.delete("/books/{title}")
async def remove_book(title: str):
    await delete_book(title)
    return {"message": "Book deleted"}
