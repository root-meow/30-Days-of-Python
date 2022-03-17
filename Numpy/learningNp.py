import numpy as np

#int array
a = np.array([1,2,3,4,5])

#int float
b = np.array([1.2,1.4,2.4,3.5,5.5])
f = np.array([1.2,2.3,1.4,4.5,5.5])

print(type (a))
print(type(b))

#Operations
#Such operations that would normally involve a for loop are alled vectorized operations
print(a*f)
print(a**f)
print(a + b)
print(f - a)

#You can do such operations between the array and a constant
print(a * 20)

#We also have universal functions known as ufuncs
print(np.sin(a))  #Gets the sin of values in array a

#Multidimensional array
ab = np.array([[1,2,3,4,5], [12,13,14,15,16]])

print(type(ab))
print(ab.ndim)
print(ab.shape)
print(ab.size)
print(ab[0, 4])  #Prints the value found at these coordinates. since it is 2D array, first, specify which set to get from, then which position in set
print(ab[1,4])   #Arrays are sequential and they can be indexed. 
print(ab[0])

#Using slices to get a row/column of values
#Slicing works the same way as in python
# var[upperbound:lowerbound:step]  the step is optional
print(ab[1][0:4:2])  #Here, I specify thatI want to pick values from the first set. From this first set I want the values starting from the first to the fourth and it takes every second value only.
print(ab[0:4])      # If you do not specify from which set to pick values, it takes values from both sets using the upper bound, lower bound and step provided.
print(ab[0][0:-2]) #The negative means starting from the end of the array where -1 is the very last value

#Omit a bound
print(ab[0][-2:])   #This prints out the last two values
print(ab[0][:3])#Prints out the first three values
print(ab[0][:-2])#Prints out values till the second last value
print(ab[1][::2])  #Only included the step. Prints from the beginning to the end
print(ab[1][::])  #Works like print(ab[1]): prints everything
print(ab[0, 1:])  #0 specifies the set to pick from. 1: specifies where to start and where to stop
print(ab[0:,2:])  #You can also specify where to start in terms of sets in the array then spacify where to start in each set
print(ab[:, 2])

#
ad = np.arange(25)
print(ad)
ac = np.arange(25).reshape(5,5)
print(ac)

#Practice
print()
yellow_row = ac[4, ::]
print(yellow_row)

print()

red_column = ac[0:, 1:4:2]
print(red_column)

print()

blue_cells = ac[1:4:2, 0:4:2]
print(blue_cells)  #Confusing as hell for starters but interesting. Find illustration in p.26, pdfs - from https://github.com/enthought/Numpy-Tutorial-SciPy-2019

#Slices in resetting values in an array position
ae = np.array([1,2,3,4,5,6,7,8]) 

slice_two = ae[-2:]
print(slice_two)
print()
slice_two = 78   #Both of the last two values are set to 78
print(slice_two)  
print()

slice_two = [78,92]
print(slice_two)

print()
ae[-2:] = 78
print(ae)
print()
ae[-2:] = [90, 92]
print(ae)

print(ae.__getitem__(0))

#fancy indexing
c = np.arange(0,80,10)

indices = [1,2,-3]  #retuns the values a these points
y = c[indices]
print(y)

#Incase of setting values
c[indices] = 90
print(c)

#Manual creation of masks
mask = np.array([0,1,1,0,0,1,0,0], dtype = bool)   # 1 - True, 0 - False
#If true, it is selected

#fancy indexing
y = c[mask]
print (y)


d = np.array([-3,-5,-1,0,2,3,4,8]) 
negative = (d < 0)

print(negative)#In this comparison, numbers less than 0 are assigned the value true and the ones above 0 are false

print(d[negative])

ad = np.array([[0,1,2,3,4,5],[10,11,12,13,14,15],[20,21,22,23,24,25],[30,31,32,33,34,35],[40,41,42,43,44,45],[50,51,52,53,54,55]])
print(type(ad))
#print(ad)
ad.reshape(6,6)
print(ad)

print(ad[[0,1,2,3,4],[1,2,3,4,5]])   #Out of row 0, pick cell 1 etc etc. 1st array = rows, second = columns
print()

print(ad[3:, [0,2,5]])

print()
mask = np.array([1,0,1,0,0,1], dtype = bool)
print(ad[mask,2])  # 2 - on which column are you applyin the mask

af = np.arange(25).reshape(5,5)
#print(af)
#indices = ([0,2,3],[2,3,[1,4]])
print(af[[0,2,3,3],[2,3,1,-1]])

print()
print(af%3) #Numbers are divied by 3 then the remainder is printed
print(af%3 == 0) #Print numbers where the remainder is 0
print(af[af%3 == 0]) #In out array where are these numbers whose remainder is 0?

#Ops on arrays
a = np.array([[1,2,3],[4,5,6]])
print()

#sum()
print(a.sum())   #Adds all the values in the array together

#Opertatind on columns or rows
print(a.sum(axis=0))   #The 0 tells numpy to add column wise.
#axis 0 is goin down -1 always going right
print()

print(a.sum(axis=-1))#Does summation row wise

#Create an array of ones
a = np.ones((5,6)) #The 5,6 is the shape. This follows (x,y) 
#Depending on dimensions, in 2D i.e (x,y) x is always -1, y is always -2
#In 3D z becomes -3
#In 4D we have all of 3D and the fourth dimension is -4
print(a)
print(a.shape)
#Collapse rows
print(a.sum(axis=-1))

print()

a = np.array([[2,3],[0,1]])
print(a)
#Prefer numpy functions to builtins when working with arrays
print(np.min(a)) #Find the minimum of a. Return the least value
#Incase wo same values for the least value, it prints it out just once.
#You can also do
print(a.min())

#You can also do max of one dimension in a multidimensional array using the axis
print(a.min(axis=0))

#Finding the location of the min/max and not the value
print(a.argmax())
print(np.where(np.argmin(a)))

#
a = np.array([-1,2,5,5])

print(a == a.max()) #Find all the coordinates that are equal to the max of a
c = np.where(a == a.max())  #Gets the maximum values of a then gives the coordinates of these values
print(c)

print()
#Find all the numbers greater than 0
c = np.where(a > 0)
print(c)


