#Assigning functions to variables
def add(a, b):
    print(a + b)
adder = add
add(5, 4)

print(add)
print(adder)

#Try
def add(a, b):
	print(a + b)

adder = add
del add

adder(5, 4)
print()

#Functions as arguments
numbers = [56, 3, 45, 29, 102, 30, 73]
highest_number = max(numbers)

print(highest_number)
print()

def get_grade_average(student):
	return student["grade_average"]

students = [
	{"name": "Hannah", "grade_average": 83},
	{"name": "Charlie", "grade_average": 91},
	{"name": "Peter", "grade_average": 85},
	{"name": "Rachel", "grade_average": 79},
	{"name": "Lauren", "grade_average": 92}
]

valedictorian = max(students, key=get_grade_average)
print(valedictorian)
print()


