from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import json
from pathlib import Path

app = FastAPI(
    debug=True
)

class Book(BaseModel):
    id: int
    title: str
    author: str
    price: int
    cover: str
    description: str


class Storage:

    def __init__(self, filename: str):
        self.filename = f"{filename}.json"

        storage_file = Path(self.filename)
        if not storage_file.is_file():
            with open(self.filename, mode='w', encoding='utf-8') as file:
                json.dump([], file, indent=4)

    def create(self, book: Book):

        with open(self.filename, mode='r', encoding='utf-8') as file:
            content: list[dict] = json.load(file)

        content.append(book.__dict__)
        with open(self.filename, mode='w', encoding='utf-8') as file:
            json.dump(content, file, indent=4, ensure_ascii=False )

    def get_book(self, book_id: int) -> dict:
        with open(self.filename, mode='r', encoding='utf-8') as file:
            books: list[dict] = json.load(file)

        for book in books:
            if book['id'] == book_id:
                return book

        raise HTTPException(detail=f'Book id #{book_id} not found', status_code=status.HTTP_404_NOT_FOUND)



book_storage = Storage('fiction')


@app.get("/")
def get_info():
    return {"status": "okm,hfvgjhgfh"}


@app.post("/create")
def create_book(new_book: Book) -> Book:
    book_storage.create(new_book)
    return new_book


@app.get("/{book_id}")
def get_book(book_id: int) -> Book:
    book = book_storage.get_book(book_id)
    return book

