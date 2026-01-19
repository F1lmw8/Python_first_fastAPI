from fastapi import FastAPI, Body

app = FastAPI()

books = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'science'}
]

@app.get("/books")
async def get_all_books():
    return books

@app.get("/books/mybook")
async def read_book():
    return {"title": "my favorite book"}

@app.get("/books/{book_title}")
async def get_book(book_title: str):
    for book in books:
        if book["title"].casefold() == book_title.casefold():
            return book
    return {"message": "Book not found"}

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    books.append(new_book)
    return new_book

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(books)):
        if books[i].get('title').casefold() == updated_book.get('title').casefold():
            books[i] = updated_book
            return updated_book
    return {"message": "Book not found"}

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(books)):
        if books[i].get('title').casefold() == book_title.casefold():
            books.pop(i)
            return {"message": "Book deleted"}
    return {"message": "Book not found"}