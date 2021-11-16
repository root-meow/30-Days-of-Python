#I am trying to learn to convert tuples to string.

numbers = [1, 2, 3, 4, 5]
numbers = str(numbers)
print(numbers)

#The output produces something that looks like a list.
#[1, 2, 3, 4, 5]
#We want it to be 1, 2, 3, 4, 5. For this we can learn the join

#Join method
project_authors = ["Mike", "Sofia", "Helen"]
project_authors = ", ".join(project_authors)

print(f"The people who worked on this project are: {project_authors}.")

#We can also do.
project_authors = ["Mike", "Sofia", "Helen"]
print(f"The people who worked on this project are: {', '.join(project_authors)}.")     #We can only join a collection of strings.

"""One thing to be aware of when using join is that we can only join collections of strings. If we have a list of numbers, we have to convert each number to a string first.

    We start with a list of numbers, called numbers.
    Then we create an empty list, stringified_numbers. This will hold our numbers converted to strings.
    Using a for loop, we iterate over the numbers list. We convert each number to a string and append it to stringified_numbers.
    Finally, we use join with stringified_numbers."""

numbers = [1, 2, 3, 4, 5]

stringified_numbers = []

for number in numbers:
	stringified_numbers.append(str(number))

print(', '.join(stringified_numbers))

#Splitting up a string
user_numbers = input("Please enter 5 numbers separated by commas: ") # 1,2,3,4,5
numbers_list = user_numbers.split(", ")
print(numbers_list)
#print(numbers_list)