# this is the main file with UI
import database

MENU_PROMPT = """
-- Coffee Bean App --

Please choose one of these options:

1) Add a new bean.
2) Delete bean by name.
3) Find bean by name.
4) See all beans.
5) See all beans by rating.
6) See which preparation method is best for a bean.
7) Exit.

Your selection: """


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "7":
        if user_input == "1":
            prompt_add_new_bean(connection)
        elif user_input == "2":
            prompt_delete_bean(connection)
        elif user_input == "3":
            prompt_find_bean(connection)
        elif user_input == "4":
            prompt_see_all_beans(connection)
        elif user_input == "5":
            prompt_see_all_bean_rating(connection)
        elif user_input == "6":
            prompt_find_best_method(connection)
        else:
            print("Invalid input, please try again!")


def prompt_add_new_bean(connection):
    name = input("Enter bean name: ")
    if not name.isalpha():
        print("Invalid name, please try again!\n")
    else:
        name = name.title()
    method = input("Enter how you've prepared it: ")
    if not method.isalpha():
        print("Invalid method, please try again!\n")
    else:
        method = method.title()
    rating = int(input("Enter your rating score (0-10): "))
    if rating < 0 or rating > 10:
        print("Invalid rating, please try again!\n")
    else:
        database.add_bean(connection, name, method, rating)

def prompt_delete_bean(connection):
    name = input("Enter bean name to delete: ")
    name = name.title()
    try:
        database.get_delete_bean(connection, name)
        print(f"Deleted all {name} beans.")
    except TypeError:
        print("Cannot find bean name!")

def prompt_see_all_beans(connection):
    beans = database.get_all_beans(connection)
    for bean in beans:
        print(f"{bean[1]} ({bean[2]}) - {bean[3]}/10")

def prompt_see_all_bean_rating(connection):
    min_rating = int(input("Enter minimum range: "))
    max_rating = int(input("Enter maximum range: "))
    beans = database.get_beans_by_rating(connection, min_rating, max_rating)
    for bean in beans(range(min_rating, max_rating)):
        print(f"{bean[1]} ({bean[2]}) - {bean[3]}/10")

def prompt_find_bean(connection):
    name = input("Enter bean name to find: ")
    name = name.title()
    beans = database.get_beans_by_name(connection, name)
    for bean in beans:
        print(f"{bean[1]} ({bean[2]}) - {bean[3]}/10")


def prompt_find_best_method(connection):
    name = input("Enter bean name to find: ")
    name = name.title()
    try:
        best_method = database.get_best_preparation_for_bean(connection, name)
        print(f"The best preparation method for {name} is: {best_method[2]}")
    except TypeError:
        print("Cannot find bean name!")


menu()
