#Join
#Can only be used on a collection of strings.

project_authors = ["Mike", "Sofia", "Helen"]

print(f"The people who worked on this project are: {', '.join(project_authors)}.")

#If we wanted to use join with numbers, we would have to change them to strings first.
numbers = [1,2,3,4,5,6]
stringified_numbers = []

for number in numbers:
    stringified_numbers.append(str(number))

print(', '.join(stringified_numbers))