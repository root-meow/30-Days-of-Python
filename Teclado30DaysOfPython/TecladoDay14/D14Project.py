#Day 14 implementation.

"""The brief

For this project the application needs to have the following functionality:

    Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
    The program should store information about all of these books in a file called books.csv, and this data should be stored in CSV format.
    Users should be able to retrieve the books in their reading list, and these books should be printed out in a user-friendly format.
    Users should be able to search for a specific book by providing a book title.
    Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program. You can see an example of a working menu in the post on while loops (day 8)."""


 #******************* Function Definition  #*******************

 #Let us try to have a single function for each functionality

# Add books function.
def add_books():
    #Take user input
    Title = input("Title: ")
    Author = input("Author: ")
    Year = input("Year: ")

    book = f"{Title}, {Author}, {Year}\n"  #\n so that new entries be made on a new line

    #Write user input to the csv file.
    #We use a context manager
    with open ("books.csv", "a") as book_file:
        book_file.write(book)

# Read books from csv and return books
def fetch_books():
    #Create an empty list to store books
    book_list = []
    with open("books.csv", "r") as book_file:
        # Iterate through the books in the list getting the Author name, Title and year of publication
        for book in book_file:
            Title, Author, Year = book.strip().split(",")
            
            # Append dictionaries with book details to the empty list
            book_list.append({
                "Title": Title,
                "Author" : Author,
                "Year of Publication" : Year
            })

    return book_list


# Function to display books in book_list
#Function takes book_list as a parameter/Argument
def display_books(book_list):

    print()
    
    for book in book_list:
        print(f"{book['Title']}, {book['Author']}, ({book['Year of Publication']})")

        print() #Prints an empty line


#Function to search for books by giving a book title
def search_books():
    list_of_books = fetch_books() #fetch_books function returns books which is what we need
    #reate a list to store the books that match the search term
    matching_books = []

    search_item = input("Please enter a book title to search: ").strip().lower()

    for book in list_of_books:
        if search_item == book["Title"].lower():
            matching_books.append(book)

    return matching_books



menu = """Please select one of the following options:

 - 'a' adds a book
 - 'l' lists books
 - 's' searches books
 - 'q' to quit

 What would you like to do? """

selected_option = input(menu).strip().lower()

# Run the loop until the user selected 'q'
while selected_option != "q":
	if selected_option == "a":
		add_books()
	elif selected_option == "l":
		# Retrieves the whole reading list for printing
		list_of_all_books = fetch_books()

		# Check that reading_list contains at least one book
		if list_of_all_books:
			display_books(list_of_all_books)
		else:
			print("Your reading list is empty.")
	elif selected_option == "s":
		matching_books = search_books()

		# Checks that the seach returned at least one book
		if matching_books:
			display_books(matching_books)
		else:
			print("Sorry, we didn't find any books for that search term.")
	else:
		print(f"Sorry, '{selected_option}' isn't a valid option.")

	# Allow the user to change their selection at the end of each iteration
	selected_option = input(menu).strip().lower()



        
        



