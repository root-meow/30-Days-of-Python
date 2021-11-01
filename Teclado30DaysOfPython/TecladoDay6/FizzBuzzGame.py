#Day 6 Mini project
#Fizz Buzz Game

#Description
"""
In case you're not familiar with the game, it goes like this:

    One player starts by saying the number 1.
    Each player then takes it in turns to say the next number, counting one at a time.
    If the number is divisible by 3, instead of saying the number, the player should say, "Fizz".
    If the number is divisible by 5, instead of saying the number, the player should say, "Buzz".
    If the number is divisible by 3and5, instead of saying the number, the player should say, "Fizz Buzz".
    If you make a mistake, you're usually eliminated from the game, and the game continues until there's only a single player remaining.
"""

#Objective
"""
For our version, we're only going to have a single player, the computer, and it's going to play the first 100 rounds of Fizz Buzz all by itself. In other words, we need to print out the first 100 items in the sequence, starting from 1.
"""

#Steps
#1. Using range create a list of numbers from 1-100
#2. Get numbers divisible by either 3 or 5 or both and print fizz, buzz and fizz buzz respectively

#Step 1

number_range = range(1,100)

#step 2
for number in number_range:
    if number %3 == 0 and number %5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number %5 == 0:
        print("Buzz")
    else:
        print(number)