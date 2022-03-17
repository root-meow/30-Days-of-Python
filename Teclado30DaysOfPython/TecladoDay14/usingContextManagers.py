#####################################Working with Context manager#####################################

#Create a file example.txt
#Write to that file

#Using context manager helps us not to have to close the file every time. 
#Closing is done automatically.
#example_file = open("example.txt", "r")
with open("example.txt", "w") as example_file:
    example_file.write("\nBig ships sailing in the ocean, \nWe don't need no commotion.")
    #print(example_file.read())

with  open("example.txt", "r") as example_file:
    print(example_file.read())







