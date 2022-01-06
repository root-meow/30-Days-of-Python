movies = [
	(
		"Eternal Sunshine of the Spotless Mind",
		"Michel Gondry",
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

for title, director, year in movies:    #In this for statement, the items are name as they follow each other in each tuple
	print(f"{title} ({year}), by {director}")