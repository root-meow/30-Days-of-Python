#1 Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget

movies = [("Fast and furious", "Mike", 2004, "$60 Million")]

#2 Use the input function to gather information about another movie. You need a title, director’s name, release year, and budget.
#Reduce wordiness
user_movie_name = input("movie name: ")
user_movie_director = input("movie director: ")
user_movie_release_year = input("year of release: ")
user_movie_budget = input("budget: ")

#3 Create a new tuple from the values you gathered using input. 
#Make sure they’re in the same order as the tuple you wrote in the movies list
#f string saves us a whole bunch of trouble
t_user_movie = (f"{user_movie_name},{user_movie_director},{user_movie_release_year},{user_movie_budget}")
print(t_user_movie)

#4 Use an f-string to print the movie name and release year by accessing your new movie tuple.

print(f"The movie you entered was {user_movie_name} and the release year is {user_movie_release_year}.")

#5 Add the new movie tuple to the movies collection using append.

movies.append(("Die Hard", "Kibet", "2002", "$210 million"))

#6 Print both movies in the movies collection.

print(movies)

#7 Remove the first movie from movies. Use any method you like

movies.pop(0)
print(movies)
