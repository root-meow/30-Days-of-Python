#Number guessing game

correct_num = 53

num = int(input('Please enter a number: '))

while num != correct_num:
    if num < correct_num:
        print('You guessed the number wrong. Your guess is too low')
        num = int(input('Please enter a number: '))
        continue
    elif num > correct_num:
        print('You guessed the number wrong. Your guess is too high')
        num = int(input('Please enter a number: '))
        continue
else:
    print('Hurrah, even when you guess you get it correct!')