from utils import database
USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """


def menu():
    while True:
        user_input = input(USER_CHOICE).upper()
        if user_input == 'Q':
            break
        elif user_input == 'A':
            prompt_add_book()
        elif user_input == 'L':
            list_books()
        elif user_input == 'R':
            prompt_read_book()
        elif user_input == 'D':
            prompt_delete_book()

# def prompt_add_book() ask for book name and author
# def list_books() show all the books in our list
# def prompt_read_book() ask for book name and change it to read in our list
# def prompt_delete_book() ask for book name and remove book from the list


def prompt_add_book():
    book_name = input("Book name: ")
    book_author = input("Author name: ")
    database.add_book(book_name,book_author)


def list_books():
    book_len = len(database.books)
    for i in range(0, book_len):
        read = 'YES' if database.books[i]["read"] else 'NO'
        print(f'{i+1}\nname: {database.books[i]["name"]}\nauthor: {database.books[i]["author"]}\nread: {read}\n\n')


def prompt_read_book():
    book_name = input("Book name: ")
    database.mark_as_read(book_name)



def prompt_delete_book():
    book_name = input("Book name: ")
    database.delete_book(book_name)
    pass


#MAIN
menu()