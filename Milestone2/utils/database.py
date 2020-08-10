import json
import sqlite3

"""
Concerned with storing and retrieving books from a list
"""

books = []


def create_tables():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key , author text, read integer)')
    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    result_set = cursor.fetchall()
    global books
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in result_set]
    connection.commit()
    connection.close()

def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
    connection.commit()
    connection.close()


def mark_as_read(name):
    book_len = len(books)
    for i in range(0, book_len):
        if name.upper() == books[i]['name'].upper():
            books[i]['read'] = True
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))
    connection.commit()
    connection.close()


def delete_book(name):
    for i in range(0, len(books)):
        if books[i]['name'] == name:
            books.remove(books[i])
            break
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE name=?', (name,))
    connection.commit()
    connection.close()


def save_all_books():
    with open('books.json', 'w') as file:
        json.dump(books, file)


get_all_books()