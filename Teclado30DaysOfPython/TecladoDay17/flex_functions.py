#The lesson today is on how to accept a variable number of arguments using *args and keyword arguments using **kwargs
#Example
# *args allows for as many names as may be possibly given
# * is an operator
# If you can use more descriptive names please avoid using args
def multigreet(*args):
    for name in args:
        print(f"Hello {name}!")

names = ["Fiona", "Savfari", "Siementa"]  #If we do this, we have to put a star befor the name of the list when passing it to the function
multigreet(*names)

multigreet ("Fiona", "Savfari", "Siementa")