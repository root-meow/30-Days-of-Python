#Try to approximate the behaviour of the is operator using ==. 
#Remember we have the id function for finding the memory address for a given value, and we can compare memory addresses to check for identity.
name1 = "Mikey Hikey"
name2 = "Mikey Dikey"
name3 = "TakeA Hikey Mikey"
name4 = "Mikey Hikey"

#Checking if the names are the same
print(name1 == name4)
#check if name1 is name 4
print(id(name1))
print(id(name2))

print(name1 is name2)

#Q2 Try to use the is operator or the id function to investigate the difference between this:
"""numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
and
numbers = [1, 2, 3, 4]
numbers.append(5)
"""

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
print(new_numbers)

number1 = [1, 2, 3, 4]
number1.append(5)
print(number1 is number1)  #number1 is number one after we append 5
print(number1)

#Using is to check the difference
print(new_numbers is number1)
print(new_numbers == numbers)  #The two are the equal but new_numbers is not numbers.


# Ask the user to enter a number. 
#Tell the user whether the number is positive, negative, or zero
user_number = float(input("Please enter a number: "))
if user_number == 0:
    print("The number you entered is 0. ")
elif user_number > 0:
    print(f"The number you entered is positive and more than 0. Infact you entered {user_number}")
else:
    print(f"You entered a negative number {user_number}. ")


#Write a program to determine whether an employee is owed any overtime. 
#You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.
#If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay, as well as the amount due. 
#The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours. 
#In effect, the employees get paid 110% of their hourly wage for any overtime.

hours_worked = int(input("How many hours has the employee worked this week: "))
hourly_wage = float(input("What is the employee's hourly wage: "))

total_wages = hourly_wage * hours_worked
overtime_pay = hourly_wage * 110/100
total_overtime_hours = hours_worked - 40
total_pay = 40 * hourly_wage + total_overtime_hours * overtime_pay

if hours_worked == 40:
    print("This employee is to be paid " + 40 * hourly_wage)
elif hours_worked < 40:
    print("This employee is to be paid: " + hours_worked * hourly_wage)
else:
    print("This employee is to be paid weekly wage of " + str(40 * hourly_wage) + " and overtime of " + str(total_overtime_hours * overtime_pay) + ". The total pay is " + str(total_pay))