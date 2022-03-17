example_file = open('txtfile.txt', "r") #Allows access to the file. You can read the file. "r" simply explicitly tells that we want to only read the file
print(example_file.read())   #Prints the content of example file. the read() function reads the contents of example_file. then this is printed
#It is good practice to close files.
example_file.close()  #When reading and printing is done, close the file