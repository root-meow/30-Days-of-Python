# Code to test and learn for loops.

#First I will create a list of movies with tuples,
#Each tuple has 3 items in the following order, Movie name, movie director and year of production.

movies = [
    (
        "Eternal Sunshine of the Spotless mind",
        "Michael Gondry",
        2004
    ),
    (
        "Memento",
		"Christopher Nolan",
		2000
    ),
    (
		"Requiem for a Dream",
		"Darren Aronofsky",
		2000
	)
]

#This part creates a var movie which stores an item from the list.
#For each item (which happens to be a tuple), print the first item in the tuple
# which happens to be the movie name then, in brackets print the second item of the selected tuple
# and after by, print the first item. Please remember computers count from 0 and not 1.
for movie in movies:
    print(f"{movie[0]} ({movie[2]}), by {movie[1]}")

#The structure of a for loop.
#Always use descriptive variable names.
"""
for variable in iterable:
    do(Specify what should be done)
"""
