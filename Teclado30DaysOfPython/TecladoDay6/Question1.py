#Q 1
"""Below we've provided a list of tuples, where each tuple contains details about an employee of a shop: 
their name, the number of hours worked last week, and their hourly rate. 
Print how much each employee is due to be paid at the end of the week in a nice, readable format."""

#What needs to be done(Goal):
#1. Have a way of calculating wages at the end of the week.
#2. Create a loop that takes each employees hours worked and hourly rate then puts them in above function.
#3. Print the result with the name attached. 


#List of employees and their data
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

#2. Create a loop that takes each employees hours worked and hourly rate then puts them in above function.

for employee in employees:
    #Define variables to be used in calculation.
    hours_worked = f"{employee[1]}" #Today I learnt I could use format like this.
    hours_worked = int(hours_worked)

    hourly_rate = f"{employee[2]}"
    hourly_rate = float(hourly_rate)
    
    #Function to calculate weekly wage.
    weekly_wage = hours_worked * hourly_rate

    #Outputting to screen
    print(f"{employee[0]} worked for {employee[1]} hrs and their hourly rate is {employee[2]}. " + "\n" + "Total weekly wage is " + str(weekly_wage) + "\n")