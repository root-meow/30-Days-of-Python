#Use the sort method to put the following list in alphabetical order with regards to the students' names:
def sort(student):
    return student["name"]

students = [
	{"name": "Hannah", "grade_average": 83},
	{"name": "Charlie", "grade_average": 91},
	{"name": "Peter", "grade_average": 85},
	{"name": "Rachel", "grade_average": 79},
	{"name": "Lauren", "grade_average": 92}
]

students.sort(key=sort)
print(students)

#Convert the following function to a lambda expression and assign it to a variable called exp.
def exponentiate(base, exponent):
	return base ** exponent
exp = lambda base, exponent: base ** exponent
print(exp(5,2))

print(exp)