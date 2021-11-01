#Ask for input

employee_name = input("Please enter the Employee name: ")
hourly_wage = input("Please enter the employees hourly wage: ")
hours_worked = input("Enter the number of hours worked: ")

#String processing.
employee_name.strip().title()

#Earnings calculator
total_pay = float(hourly_wage) * float(hours_worked)

#Output as a single string.
print(f"{employee_name} earned {total_pay} this week.")
