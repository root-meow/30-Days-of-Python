#Slices

sample_string = "Python"
sliced_string = sample_string[0:3] #Give back the items from the string from position 0 to 3
#Takes every item up to but not inclusive of item at index 3
print(sliced_string)

"""#We could also do
sample_string = "Python"
sliced_string = sample_string[3:] #We have not specified the start. Python starts from the beginning.
                                  #If we do not specify the end, it eill run till the end.
print(sliced_string)"""

#We can also use negative indices. 
#We learnt that negative indices count from the back/end
#If we use negative indices here, we tell Python not to include the items covered by those indices.

sample_string = "Python"

print(sample_string[3:])
print(sample_string[3:-2])