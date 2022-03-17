#Rewrite this code using a context manager.

""" f = open("hello_world.txt", "w)
    f.write("Hello, World!")
    f.close()
"""

#Using the context manager.
with open("hello_world.txt", "w") as hello_world_file:
    hello_world_file.write("Hello, World!")
with open("hello_world.txt", "r") as hello_world_file:
    print(hello_world_file.read())