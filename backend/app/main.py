from fastapi import FastAPI
from app.crud import create_book, get_books, update_book, delete_book
from app.models import Book

app = FastAPI()

@app.post("/books/")
async def add_book(book: Book):
    return await create_book(book)

@app.get("/books/")
async def read_books():
    return await get_books()

@app.put("/books/{book_id}")
async def edit_book(book_id: str, book: Book):
    return await update_book(book_id, book)

@app.delete("/books/{book_id}")
async def remove_book(book_id: str):
    return await delete_book(book_id)
