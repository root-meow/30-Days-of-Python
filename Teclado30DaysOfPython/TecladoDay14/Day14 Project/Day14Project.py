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


#Day 14 implementation.

"""The brief

For this project the application needs to have the following functionality:

    Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
    The program should store information about all of these books in a file called books.csv, and this data should be stored in CSV format.
    Users should be able to retrieve the books in their reading list, and these books should be printed out in a user-friendly format.
    Users should be able to search for a specific book by providing a book title.
    Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program. You can see an example of a working menu in the post on while loops (day 8)."""



#********************************************* Try to use SRP (Single Responsibility Function) *********************************************


menu_options = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 's' to search books
- 'q' to quit

What would you like to do? """

#book_list = []

#Function definition
def add_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year of publication: ").strip()
    book = f"{title},{author},{year}\n"
    with open ("book.csv", "a") as book_file: #context managerthat opens and automaticallycloses files after working on them. "a" is append.
        book_file.write(book) #Writes to the file. New details are added to the end of the end of the files.


def get_books(): 
    books = [] #Create an empty list called books

    with open ("books.csv", "r") as reading_list:  #Context manager to open books.csv and read.
        for book in reading_list:
            Title,Author,Year = book.strip().split(",")  #The title, author and year are separated by commas. These three form one book.
            #Dictionary with book details. 
            #Dictionaries take the form "name" : value 
            #Appends the dictionary to a list
            books.append({
                "Title": Title,
                "Author": Author,
                "Year": Year
            })
    #This function returns the books list which is now populated with the dictionaries for each book.
    return books

def display_booklist(books):  #takes a parameter books from get_books()

    print()    #Prints an empty line

    #with open("books.csv", "r") as reading_list:
    for book in books:
        #Title = book[0]
        #Author = book[1]
        #Year = book[2]
        Title,Author,Year = book.values()
        print('Title: ' + Title + '\n' + 'Author: ' + Author + '\n' + 'Year: ' + Year)

        print()


def search_books():
    read_list = get_books()
    matching_books = input("Please enter the book you want to search for: ").stript().lower()
    for book in read_list:
        if search_term in book["Title"].lower():
            matching_books.append(book)
    
    return matching_books
selected_option = input(menu_options).strip().lower()


while selected_option != "q":
    if selected_option == "a":    #If selected option is a, call add book function 
        add_book()
    elif selected_option == "l":  #If selected option is l, call display_booklist function
        reading_list == get_books()
        if reading_list:
            display_booklist(reading_list)
        else:
            print("Please add a book to the list first!")
    elif selected_option == 's':
        matching_books = search_books()

        if matching_books:
            display_booklist(matching_books)
        else:
            print("Sorry, no books match your search.")
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")

    # Allow the user to change their selection at the end of each iteration
    selected_option = input(menu_options).strip().lower()   #The program does not stop but asks this again.





