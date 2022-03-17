#Returning functions from other functions
# Define some functions
def add(a, b):
	print(a + b)

def subtract(a, b):
	print(a - b)

def multiply(a, b):
	print(a * b)

def divide(a, b):
	if b == 0:
		print("You can't divide by 0!")
	else:
		print(a / b)

operations = {
	"a": add,
	"s": subtract,
	"m": multiply,
	"d": divide
}

selected_option = input("""Please select one of the following options:

a: add
s: subtract
m: multiply
d: divide


What would you like to do? """)

operation = operations.get(selected_option)  #Get method is used here. 
#while (selected_option := input(selected_option).strip().lower()) != "q":
if operation:
	a = int(input("Please enter a value for a: "))
	b = int(input("Please enter a value for b: "))

	operation(a, b)
else:
	print("Invalid selection")
print()

#Lambda expressions
#We can have 
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

#Or use lambda expression like so
students = [
	{"name": "Hannah", "grade_average": 83},
	{"name": "Charlie", "grade_average": 91},
	{"name": "Peter", "grade_average": 85},
	{"name": "Rachel", "grade_average": 79},
	{"name": "Lauren", "grade_average": 92}
]

valedictorian = max(students, key=lambda student: student["grade_average"])
print(valedictorian)
print()

#We can have this for the calculator
def divy(a,b):
    if b == 0:
        print('You cannot divide by 0')
    else:
        return a / b
operations = {
    'a' : lambda a,b: a + b,
    's' : lambda a,b: a - b,
    'm' : lambda a,b: a * b,
    'd' : divy
    #'d' : lambda a,b: a / b  #Lambda expressions are limited to single expressions
}

selected_option = input("""Please select one of the following options:

a: add
s: subtract
m: multiply
d: divide
q: quit #test

What would you like to do? """)

operation = operations.get(selected_option)

if operation:
	a = int(input("Please enter a value for a: "))
	b = int(input("Please enter a value for b: "))

	print(operation(a, b))
else:
	print("Invalid selection")