#List comprehensions
names = ['mary','Richard','Noah','KATE']

#We want to make all of them title case
#We could do

names_processed = []

for name in names:
    names_processed.append(name.title())
print(names_processed)
print()

#The above code is quite verbose
#What if we could use a list cmprehension
names = [name.title() for name in names]
print(names)
print()
#This above code does what we did with the for loop above with fewer lines

#We can do it for even more complex situations
ages = (36, 21, 40, 28)

people = []

#We can do
for name, age in zip(names, ages):
    #person = (name.title(), age)
    #people.append(person)
    #print(people)
    #Can we just do
    people.append((name.title(), age)) #This works.
print(people)
print()

#We can do
people = [(name.title(), age) for name, age in zip(names, ages)]
print(people)
print()

#Set comprehensions
#Why would we want to use sets instead of lists
names = {name.title() for name in names}
print(names)
print()

#Dictionary comprehensions
#Dictionaries go ("name": value)
#We can do
student_ids = (112343, 134555, 113826, 124888)
names = ("mary", "Richard", "Noah", "KATE")

students = {}

for student_id, name in zip(student_ids, names):
	student = {student_id: name.title()}
    #students.append(student)
	students.update(student) #Can we use append instead

print(student)
print(students)
print()

#We can use a comprehension to do
students = {student_id: name.title() for student_id, name in zip(student_ids, names)}
print(students)
print()

names = ["Matthew", "John", "Helen", "Stephen", "Alexandra", "Rolf"]
#Adding conditionals
names = [name for name in names if len(name)>6]
print(names)
print()

names = ["Matthew", "John", "Helen", "Stephen", "Alexandra", "Rolf"]
short_final_name = [
    name for name in names
    if len(name) < 6
    if name[-1] == "n"
    ]
print(short_final_name)
