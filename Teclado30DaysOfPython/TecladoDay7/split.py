user_numbers = input("Please enter 5 numbers separated by commas: ") # 1, 2, 3, 4, 5
numbers_list = user_numbers.split(",") #This line is so that, everywhere where a , is encountered, that is seen as the end of one list item.

print(numbers_list) 


#Code for when we want to remove spaces in user input
user_numbers = input("Please enter 5 numbers separated by commas: ") # 1, 2, 3, 4, 5
user_numbers = user_numbers.split(",")

numbers_list = []

for number in user_numbers:
	numbers_list.append(number.strip())

print(numbers_list)