from fastapi import FastAPI
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
            json.dump(content, file, indent=4)


book_storage = Storage('fiction')


@app.get("/")
def get_info():
    return {"status": "okm,hfvgjhgfh"}


@app.post("/create")
def create_book(new_book: Book) -> Book:
    book_storage.create(new_book)

    return new_book