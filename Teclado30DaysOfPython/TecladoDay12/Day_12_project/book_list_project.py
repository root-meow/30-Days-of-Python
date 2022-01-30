"""Welcome to the Day 12 project in 30 Days of Python! We're going to create a program that can store and display books from a user's 
reading list.

Down below you'll find a full project brief as well as a walkthrough for our solution. Remember your solution doesn't 
have to match ours exactly!
§
The brief

For this project the application needs to have the following functionality:

    1. Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
    2. The program should store information about all of these books in a Python list.
    3. Users should be able to display all the books in their reading list, and these books should be printed out in a user-friendly 
    format.
    4. Users should be able to select these options from a text menu, and they should be able to perform multiple operations without
    restarting the program. You can see an example of a working menu in the post on while loops (day 8)."""


menu_options = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 'q' to quit

What would you like to do? """

book_list = []

def add_book():
    book = (input("Please enter a book you like in this format: book title, author's name, and year of publication. ")).split(",")
    book_list.append(book)

def display_booklist():
    for book in book_list:
        Title = book[0]
        Author = book[1]
        Year = book[2]
        print('Title: ' + Title + ' | Author: ' + Author + ' | Year: ' + Year)

selected_option = input(menu_options).strip().lower()

while selected_option != "q":
    if selected_option == "a":    #If selected option is a, call add book function 
        add_book()
    elif selected_option == "l":  #If selected option is l, call display_booklist function
        if book_list == []:
            print("Please add a book to the list first!")
        else:
            display_booklist()
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")

    # Allow the user to change their selection at the end of each iteration
    selected_option = input(menu_options).strip().lower()





