"""
For this harder version of the project, the application needs to have the following functionality:

    Users should be able to add a book to their reading list by providing a book title, an author's name, a year of publication, and whether or not the book has been read.
    The program should store information about all of these books in a file called books_details.csv, and this data should be stored in CSV format.
    Users should be able to retrieve the books in their reading list, and these books should be printed out in a user-friendly format.
    Users should be able to search for a specific book by providing a book title.
    Users should be able to mark a book as read by entering a book title. If there are multiple books with the same title, you can just mark the first matching book as read.
    Users should be able to delete books from their reading list by providing the book title for the book they want to delete. Once again, you can just delete the first matching book.
    Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program.

"""

#SRF (Single Responsibility Function)
# There should be an update function that writes to the file

# Add book function
def add_book():
    #Ask user input of title, author, year of publication and read status
    title = input("Title: ")
    author = input("Author: ")
    year_of_publication = input("Year: ")
    read_status = input("Read Status: ")

    #Tell Py that all these details are asociated to entity "book" remove white space and change to lowercase
    #title, author, year_of_Publication, read_status = book.strip().lower() 

    #Write these details to a csv file
    with open("book_details.csv", "a") as book_details:
        book_details.write(f"{title},{author},{year_of_publication},{read_status}\n")

#Function to retrieve books from a file. 
#Since we are reading from a separate file, we must first retrieve then display

def retrieve_books():
    #First we open file where books are stored
    #When retrieved, we must store them in a list

    retrieved_books = []

    with open("book_details.csv", "r") as book_details:
        #Iterate through the list of books and separate the different details at the comma
        for book in book_details:
            title, author, year_of_publication, read_status = book.strip().split(",")

            #Create a dictionary, after all, we need to print them in a user friendly format
            retrieved_books.append({
                "title" : title,
                "author" : author,
                "year_of_publication" : year_of_publication,
                "read_status" : read_status

            })

    return retrieved_books

#Function to display the books in the book file
def display_books(retrieved_books):
    print()
    
    for book in retrieved_books:
        print(f"{book['title']}, {book['author']}, ({book['year_of_publication']}) - {book['read_status']}")

        print() #Prints an empty line

#Function to search for a book using the book title
def search_book():
    #Borrow retrieved books from the retrieve books function
    retrieved_books = retrieve_books()  #Do this because retrieve_books() returns all the books

    matching_books = []
    #What book title do you want to search
    book_search_term = input("Please enter the book title: ")

    for book in retrieved_books:
        if book_search_term.lower() == book["title"].lower():
            matching_books.append(book)

    return matching_books


#Function to mark books as read
def mark_read():
     
    #Take all books as returned by search books function
    #For particular book, alter the last var, i.e the read_status
    #Save that change then write to csv file

    #Get a list of all books in file
    retrieved_books = retrieve_books()

    #Accept user input to select a book they want to mark as read.
    #book_to_mark = input("Please enter the title of the book you want to mark as read: ")

    #Take the books that match search item
    matching_books = search_book()
    #print(matching_books)  #Test to see if it works till here

    for book in matching_books:
        #if book['title'].strip().lower() == matching_books[0]['title'].strip().lower():
        retrieved_books.remove(book)
        book['read_status'] = "Read"
        retrieved_books.append(book)
        print("Read status changed to - Read.")
        
    #update_file()
    with open("book_details.csv", "w") as book_details:
        for book in retrieved_books:
            book_details.write(f"{book['title']},{book['author']},{book['year_of_publication']},{book['read_status']}\n")

        #Write changes to file
        #with open("book_details", "w") as book_details:
        #    book_details.write(f"{book['title']},{book['author']},{book['year-of_publication']},{book['read_status']}\\n")

#Function to delete books.
def delete_entry():
    #Take user input. Which book to delete
    #Take list of all books
    #Pop from list user entered book
    #Write changes to file

    #Take list of all books
    retrieved_books = retrieve_books()
    matching_books = search_book()

    #Ask for book to delete
    #book_to_delete = input("Please enter a book title to delete: ")

    #Remove book from book list
    if matching_books:
        retrieved_books.remove(matching_books[0])
    #for book in retrieved_books:
     #   if book['title'].strip().lower() == book_to_delete.strip().lower():
      #      retrieved_books.remove(book_to_delete)
       #     print(f"{book['title']} deleted")

        #else:
         #   print("The selected book does not exist!")

    #Write changes to file
    #update_file()
        with open("book_details.csv", "w") as book_details:
            for book in retrieved_books:
                book_details.write(f"{book['title']},{book['author']},{book['year_of_publication']},{book['read_status']}\n")
    else:
        print("Sorry. No books match that search!")

    #return retrieved_books
    #update_file(retrieved_books)

    
    #with open("book_details", "w") as book_details:
    #   for book in retrieved_books:
    #        book_details.write(f"{book['title']},{book['author']},{book['year_of_publication']},{book['read_status']}\n")

#Function to update file
# def update_file(retrieved_books):
#    with open("book_details.csv", "w") as book_details:
#        for book in retrieved_books:
#            book_details.write(f"{book['title']},{book['author']},{book['year_of_publication']},{book['read_status']}\n")





menu = """Please select one of the following options:

 - 'a' adds a book
 - 'd' to delete book
 - 'l' lists books
 - 'm' to mark as read
 - 's' searches books
 - 'q' to quit

 What would you like to do? """

#selected_option = input(menu).strip().lower()

while (selected_option := input(menu).strip().lower()) != "q":   #Assignment operation reduces redundancy
    if selected_option == "a":
        add_book()
    elif selected_option == "d":
        delete_entry()
    elif selected_option == "l":
        retrieved_books = retrieve_books()

        if retrieved_books:  #If true i.e if it has content
            display_books(retrieved_books)
        else:
            print("Your reading list is empty.")
    
    elif selected_option == "m":
        mark_read()
    elif selected_option == "s":
        matching_books = search_book()

		# Checks that the seach returned at least one book
        if matching_books:
            display_books(matching_books)
        else:
            print("Sorry, we didn't find any books for that search term.")
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")

	# Allow the user to change their selection at the end of each iteration
    #selected_option = input(menu).strip().lower()

    





