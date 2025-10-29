from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    debug=True
)


class NewBook(BaseModel):
    id: int
    title: str
    author: str
    price: int
    cover: str
    description: str




@app.get("/")
def get_info():
    return {"status": "okm,hfvgjhgfh"}


@app.post("/create")
def create_book(new_book: NewBook) -> NewBook:
    print(new_book)
    return new_book