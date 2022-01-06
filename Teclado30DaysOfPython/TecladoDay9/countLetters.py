#Using  enumerate to count the number of letters in a word

word = input('Please enter a word: ')

for counter, letter in enumerate(word, start = 1):
    print(f"{counter}. {letter} ")
    continue
    word = input('Please enter a word: ')
    

    

