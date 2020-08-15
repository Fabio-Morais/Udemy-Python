from app import books

USER_CHOICE = """Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalogue
- 'q' to exit

Enter your choice: """

def print_best_books():
    best_books = sorted(books, key=lambda x: -x.rating)
    x = [i for i in best_books if i.rating == 5]
    for i in x:
        print(i)

def print_cheapest_books():
    best_books = sorted(books, key=lambda x: (x.price))[:10]
    for book in best_books:
        print(book)


books_generator = (x for x in books)


def get_next_book():
    print(next(books_generator))

user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}

def menu():
    while True:
        user = input(USER_CHOICE)
        if(user == 'q'):
            break
        elif(user in ('b','c','n')):
            user_choices[user]()


menu()