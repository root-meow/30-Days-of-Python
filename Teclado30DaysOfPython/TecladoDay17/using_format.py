"""people = [
	("Bob", 42, "Mechanic"),
	("James", 24, "Artist"),
	("Harry", 32, "Lecturer")
]"""

people = [
    {
        "name": "Bob",
        "age": 42,
        "occupation": "Mechanic"
    },
    {
        "name": "James",
        "age": 24,
        "occupation": "Artist"
    },
    {
        "name": "Harry",
        "age": 32,
        "occupation": "Lecturer"
    }
]

for person in people:
    for key, value in person.items():
        print(f"{key} : {value}")