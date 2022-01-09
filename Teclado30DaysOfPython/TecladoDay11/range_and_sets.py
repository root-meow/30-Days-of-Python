#Let user enter a number
user_number = int(input("Please enter a number: "))
range_given = range(3,10)



if user_number < 3:
    print("The number is too low")
elif user_number > 10:
    print("The number is too high")
elif user_number in range_given:
    print("Hurrah! The number you gave is within the range I gave. We are good together.")