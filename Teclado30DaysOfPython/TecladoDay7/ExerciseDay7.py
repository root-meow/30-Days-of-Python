#Day 7 exercises
# Q1  Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names, and then assign each name to a different variable. For this exercise, you can assume that the user has a single given name and a single surname.

#name = input("Please enter your given name and surname. Separate them with a space: ")
#name_tuple = tuple(name.split(" "))
#given_name = name_tuple[0]
#surname = name_tuple[1]
#print(f"Your given name is {given_name} and your surname is {surname}")

"""for item in name_tuple:
    print(f"Your given name is {item[1]}")
    #surname = item(1)
    
#print(given_name)"""

#Q2 Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. Remember that you can only join collections of strings, so you’re going to need to do some initial processing of the list of numbers.
numbers_list = [1, 2, 3, 4, 5]
stringified_numbers = []
for number in numbers_list:
	stringified_numbers.append(str(number))

print('|'.join(stringified_numbers))

#Q3 Each quote is a string, but each string actually contains quote characters at the start and end. Using slicing, extract the text from each string, without these extra quote marks, and print each quote.

#You may also want to try a solution using strip.

Quotes = [
 	"'What a waste my life would be without all the beautiful mistakes I've made.'",
 	"'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
 	"'The very essence of romance is uncertainty.'",
 	"'We are not here to do what has already been done.'"
 ]
for quote in Quotes:
    #quotemarks_removed = quote.strip("")
    quotes_removed = quote.strip("''")
    print(quotes_removed)

#Q4 Ask the user to enter a word, and then print out the length of the word. You should account for any excess whitespace in the user’s input, so you’re going to have to process the string before you find its length.

#If you want to take this a little bit further, you an ask the user for a long piece of text. You can then tell them how many how many characters are in the text overall, and you can also provide them a word count.

user_input = input("Please type in whatever is on your mind, I will do my magic and tell you some numbers: ")
for text in user_input:
    word = len(user_input.split())
print(word)