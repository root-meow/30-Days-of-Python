# **kwargs can be used to deal with a number of keywords
# Example
#Since dict does not know how many keys and values we want to pass, it has to be flexible
dict(name = "Phil", age = 23, city = "Budapest", nationality = "British")

#Let us try
def prety_print(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

prety_print(title = "The Matrix", diretor = "Wachowski", year = 1999)
print()

#Using * and ** to unpack
numbers = [1,2,3,4,5]
print(*numbers, sep = "|")

#Unpack a dictionary
def print_movie(*args):
    for value in args:
        print(value)
movie = {
    "title" : "The Matrix",
    "director" : "Wachowski",
    "year" : 1999
}

print(*movie.values())
print(*movie.keys())
print()

#We can also use ** to turn a dictionary into a series of keyword arguments
#Example
#Here when we do **movie when calling the function, it turns the dictionary into keyword arguments. 
#These are passed to print_movie, and the **kwargs parameter collects them back into a dictionary.
def print_movie(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

movie = {
    "title": "The Matrix",
	"director": "Wachowski",
	"year": 1999
}

print_movie(**movie)
print()

#test
# def print_movie(movie_details):
#	for key, value in movie_details.items():
#		print(f"{key}: {value}")
#
#movie = {
#	"title": "The Matrix",
#	"director": "Wachowski",
#	"year": 1999
#}
#
#print_movie(movie, studio="Warner Bros")

#We can do this, however instead of the above
def print_movie(**kwargs):
	for key, value in kwargs.items():
		print(f"{key}: {value}")

movie = {
	"title": "The Matrix",
	"director": "Wachowski",
	"year": 1999
}

print_movie(studio="Warner Bros", **movie)
