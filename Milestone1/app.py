movies = []


def add():
    name = input("Name of the movie ")
    director = input("Director of the movie ")
    year = input("year of the movie ")

    movies.append({"name": name, "director" : director, "year" : year})
    print("123")


def show():
    print("-------\nLIST\n")
    for x in movies:
        print(f"title of movie = {x['name']}")
        print(f"director of movie = {x['director']}")
        print(f"year of movie = {x['year']}")
    print("-------\n")


def f(input):
    return {
        'a': add,
        'l': show,
        'q': 1
    }.get(input, -1)


def menu_text():
    menu_prompt = """a- add new movie
l- show all the movies
q- quit the menu\n->"""
    return input(menu_prompt)


def menu():
    while True:
        user_input = menu_text()
        function = f(user_input)
        if function != 1 and function != -1:
            function()
        elif function == 1:
            break
        elif function == -1:
            print("wrong key")


menu()
