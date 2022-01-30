#Take user input and put that in title case.
name = input("Please enter your name: ")
name_in_Title_case = name.title()

#if statement to make sure you do enter a name.
if name:
    print(f"You have entered {name_in_Title_case}")
else:
    print("To proceed you must enter a name! ")