#Create a function that accepts any number of numbers as positional arguments and prints the sum of those numbers. 
#Remember that we can use the sum function to add the values in an iterable.
# Args is given to a function as a list

def summation(*numbers):
    for number in numbers:
        print(sum(number))

numbers = [10,20,30,40,50]
summation(numbers)
print()

# Create a function that accepts any number of positional and keyword arguments, and that prints them back to the user. 
#Your output should indicate which values were provided as positional arguments, and which were provided as keyword arguments.
def args_printer(*args, **kwargs):
    print(f"{args} are positional arguments.")
    print(f"{kwargs} are keyword arguments.")

args_printer(1,  "blue",  [1,  23,  3], height=184, key=lambda x: x ** 2)

#3) Print the following dictionary using the format method and ** unpacking.

def unpack(**country):
    print("{name}, {population}, {capital}, {currency}".format(**country))

country = {
    
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
}

unpack(**country)
#4) Using * unpacking and range, print the numbers 1 to 20, separated by commas. 
#You will have to provide an argument for print function's sep parameter for this exercise.
def unpack_nums(*numbers):
    print(*numbers, sep=",")

numbers = range(1,21)
unpack_nums(*numbers)
print()

#5) Modify your code from exercise 4 so that each number prints on a different line. 
#You can only use a single print call.
def unpack_nums(*numbers):
    for number in numbers:
        print(number)

numbers = range(1,21)
unpack_nums(*numbers)
print()

def unpack_nums(*numbers):
    print(*numbers, sep="\n")

numbers = range(1,21)
unpack_nums(*numbers)
print()