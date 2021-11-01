#Q1 Ask the user for their name and age, assign these values to two variables, and print them.

name = input('Please enter your name:  ')
age = input('Please enter your age: ')

#print(name + '\n' + age) #This could be print(name + '\n' + age)

mylist = [name, age]
for i in mylist:
    print(i)


#Q2 Investigate what happens when you try to assign a value to a variable that you’ve already defined. Try printing the variable before and after you reuse the name.

name = "Joe"
print(name)
name = "Mike"
print(name)

#The var takes the new value.
