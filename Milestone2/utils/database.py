import json

"""
Concerned with storing and retrieving books from a list
"""

books = []


def get_all_books():
    with open("books.json", "r") as file:
        data = json.load(file)
        for i in data:
            books.append(i)


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})
    save_all_books()


def mark_as_read(name):
    book_len = len(books)
    for i in range(0, book_len):
        if name.upper() == books[i]['name'].upper():
            books[i]['read'] = True
    save_all_books()


def delete_book(name):
    for i in range(0, len(books)):
        if books[i]['name'] == name:
            books.remove(books[i])
            break
    save_all_books()


def save_all_books():
    with open('books.json', 'w') as file:
        json.dump(books, file)


get_all_books()