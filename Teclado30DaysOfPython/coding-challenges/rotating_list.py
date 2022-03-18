#Single Clockwise rotation
base = [1,2,3,4,5]
last_value = base.pop() #This removes the last value in our list
rotated_list = [last_value] + base  #This prepends the last value to the new base list missing the last value
print(rotated_list)

#You can also use insert method
base = [1,2,3,4,5]
last_value = base.pop()
base.insert(0, last_value) #This puts the popped value at position 0 of the new base list
print(base)
print()

#We can use slicing
base = [1,2,3,4,5]
rotated_list = base[-1:] + base[:-1]  #This takes the elements in the list from position 1 (remember we use 0 index), to the end and concatenates that to a list containing only elements from list (base) starting from position 0 to position 1
print(rotated_list)
print()