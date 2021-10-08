#Day 2: Asabeneh 30 days of Python Programming

#Variable declaration.
first_name = "Mike"
last_name = "All"
full_name = "Mike All"
country_of_origin = "Uganda"
city = "Kampala"
age = "23"
year_of_birth = "1999"
is_married = "No"
is_true = "Yes"
is_light_on = "Yes"

#Create multiple variables on the same line.

name, current_year, sex = "Jane Doe", "3rd year", "Female"
print(name, current_year, sex)

#Check the data type of these variables.

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country_of_origin))
print(type(city))
print(type(age))
print(type(year_of_birth))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#Find the length of your first name.

print(len(first_name))

#Compare the length of your first name and your last name.

first_name_length = len(first_name)
last_name_length = len(last_name)
print(f"Your first name is {first_name_length} characters long, while your last name is {last_name_length} characters long.")

#Calculations

#Variable declaration.
num_one = 5
num_two = 4

#Addition
total = num_one + num_two
print(total)

#Subtraction
diff = num_two - num_one
print(diff)

#multiplication
product = num_one * num_two
print(product)

#Division
division = num_one/num_two
print(division)

#modulus
remainder = num_two % num_one
print(remainder)

#Power
exp = pow(num_one, num_two)
print(exp)

#floor division
floor_division = num_one // num_two
print(floor_division)

#Calculating the area of a circle
radius = 30
area_of_circle = 3.14 * pow(30, 2)
print(area_of_circle)

#Circumference
circum_of_circle = 3.14 * (30 * 2)
print(circum_of_circle)

#Take radius per user input and calculate area.
user_radius = input("Please enter the radius: ")
#Convert user input to float
num_user_radius = float(user_radius)
#Calculate area
user_area_of_circle = 3.14 * pow(num_user_radius, 2)
#print output
print(user_area_of_circle)

#Using input() to collect information from the user.
user_first_name = input("Please enter your first name: ")
#Formatting user input to remove white space and put input in title case
stripped_user_first_name = user_first_name.strip()
title_user_first_name = stripped_user_first_name.title()

user_last_name = input("Please enter your last name: ")
stripped_user_last_name = user_last_name.strip()
title_user_last_name = stripped_user_last_name.title()

user_country = input("Please enter your country: ")
stripped_user_country = user_country.strip()
title_user_country = stripped_user_country.title()

user_age = input("Please enter your age as a number: ")
user_age_number = int(user_age)

print(title_user_first_name, user_last_name + '\n' + user_country + '\n' + user_age)

#Run help('Keywords') to get Python reserved keywords.
import sys
help('keywords')
