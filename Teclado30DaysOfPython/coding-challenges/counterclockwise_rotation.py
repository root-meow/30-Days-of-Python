#Counterclockwise rotation one step
base = [1,2,3,4,5]
x = base.pop(0)  #removes the value at position 0 which is 1
#print(base)  #test
#base.insert(-1, x)  This does not work as I thought it would
base.append(x)  #This works. 
#We can also do
#base = base + x  This needs x to be a list. You can only concatenate a list with another list
print(base)
print()

#Using slicing
# I think slicing is better as we need not create a new list
base = [1,2,3,4,5]
base = base[1:] + base[:1]
print(base)