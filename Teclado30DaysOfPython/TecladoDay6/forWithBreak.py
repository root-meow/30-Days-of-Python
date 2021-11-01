#Start
#Create a list of movies

movies = [
    
	(
		"Eternal Sunshine of the Spotless Mind",
		"Michel Gondry",
		2004
	),
	
	(
		"Requiem for a Dream",
		"Darren Aronofsky",
		2000
	),
    (
		"Memento",
		"Christopher Nolan",
		2000
	)
]

#For statement with break
for movie in movies:            #Please note the colon at the end of both the for and if statements
    if movie[0] == "Memento":           #Check if the title of the movie is Memento
        print("Memento is in the movie library!") #If the movie is Memento, print this and stop the loop.
        break