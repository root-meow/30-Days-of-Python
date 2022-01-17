#Little program to check if a word is a palindrome

#Get word from user.
word = input("Please enter a word: ")


def palindrome_checker(word):
    word = word.strip().upper() #To remove any white spaces and capitalize all letters
    word_list = list(word)

    #print(word_list) test

    reversed_word = word_list.copy()# I do not know why reversed word = word list.reverse() does not work
    word_list.reverse()

    #print(reversed_word) test
    #reversed_word_list = 

    if word_list == reversed_word:
        print('This is a palindrome. ')

    else:
        print('This is not a palindrome. ')



palindrome_checker(word)
