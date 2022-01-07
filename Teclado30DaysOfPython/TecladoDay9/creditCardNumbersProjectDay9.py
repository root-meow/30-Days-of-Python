"""
The program you write for this project should do the following:

1) It should be able to accept a card number from the user. For this project, you can assume that the number will be entered as a single string of characters (i.e. there won't be any spaces between the numbers). However, you should be able to accept a card number with spaces at the start or end of the string.

If you want to challenge yourself, you should try to be more versatile with regards to the format that you accept card numbers in.

You may want to turn the user's input into a list of numbers, as that will make it easier to work with.

2) The program should validate that card number using the Luhn algorithm described above. You should implement this algorithm yourself.

After removing the checking digit and reversing the card number, you'll need a for loop to go over the credit card numbers. As you go through each digit, you must find a way to determine whether a digit is in an odd or an even position. Remember you can check the model solution if you get stuck!

3) Once the validation is complete, the program should inform the user whether or not the card number is valid by printing a string to the console.
"""

#******************************Taking user input******************************

#Takes user input and enters it into a list. List items are iterable.
credit_card_num = list(input("Please enter your credit card number: "))

#******************************Validating user input******************************
#let us use Luhn algorithm

#step 1. remove right most digit.
credit_card_number = credit_card_num.pop()

#step 2. 
credit_card_number = reversed(credit_card_number)
print(credit_card_number)

#Step 3. Take number at even indices and double. If above 9, subtract 9
for index, number in enumerate(credit_card_number):
    if index % 2 == 0:
        number = int(number) * 2
        if number > 9:
            number = number - 9
    else:
        continue

#Step 4. Add all numbers in list
for number in credit_card_number:
    number = int(number)
total_numbers = sum(credit_card_number)

#step 5. If the result is divisible by ten, number is valid
if total_numbers % 10 == 0:
    print("This credit card number is valid.")

else:
    print("Invalid credit card number. ")
