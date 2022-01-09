#Define functions add, subtract, divy amd multiply

def add (left_operand, right_operand):
    output = left_operand + right_operand
    print(output)

    
add(4,5)

def subtract(no_1, no_2):
    difference = no_1 - no_2
    print(difference)


subtract(no_1 = 5, no_2 = 3)


def divy(first_no, second_no):
    if second_no == 0:
        print("You cannot divide by 0.")
    elif second_no != 0:
        result = first_no / second_no
        print(result)


divy(4,6)

def multiply (num_1, num_2):
    product = num_1 * num_2
    print(product)

multiply(6,5)


#Q2

def print_show_info(tv_show):
    


#show = {
#	"title": "Breaking Bad",
#	"seasons": 5,
#	"initial_release": 2008
#}

    for item in series:
        print(f"{series['title']} ({series['initial_release']}) - {series['seasons']} seasons")

series = [
 	{"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
 	{"title": "Fargo", "seasons": 4, "initial_release": 2014},
 	{"title": "Firefly", "seasons": 1, "initial_release": 2002},
 	{"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
 	{"title": "True Detective", "seasons": 3, "initial_release": 2014},
 	{"title": "Westworld", "seasons": 3, "initial_release": 2016},
 ]


print_show_info(series)