#Len

sample_string = "Python"
print(str(len(sample_string)) + "\n")

sample_tuple = (1,2,3,4,5)
print(str(len(sample_tuple)) + "\n")

sample_list = [             #Here Python gives the #of tuples in the list.
    (1,2,3,4,5),
    (1,2,3,4,5,6),
    (1,2,3,4,5,6,7)
]
for item in sample_list:

    print(len(item))
print("The list is " + str(len(sample_list)) + " items long")