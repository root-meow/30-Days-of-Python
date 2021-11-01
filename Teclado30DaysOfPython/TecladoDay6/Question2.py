#Q2. For the employees above, print out those who are earning an hourly wage above average.

# What is the goal. To print out employees earning above average.
# What is the average? Creae a way to calculate this.
# Compare the hourly_rate with the average
# If it is above average, output the employee name.

#List
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

#1. Getting the average


total_hourly_rate = 0
number_of_employees = 0

for employee in employees:
    #Define variables
    hourly_rate = employee[2]
    hourly_rate = float(hourly_rate)
    total_hourly_rate += hourly_rate
    number_of_employees = number_of_employees + 1
    average_hourly_rate = total_hourly_rate / number_of_employees
    if hourly_rate > average_hourly_rate:
        print(f"{employee[0]} earns an hourly rate above average")

