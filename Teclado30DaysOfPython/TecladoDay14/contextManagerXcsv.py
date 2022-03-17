##################################### Working with csv data#####################################

#Tiny reminder of dictionaries
#CSV = Comma Separated Values
#csv_data = {
#   "iris1": "52cm",
#  "iris2": "40cm",
# "iris3": "30cm"
#}

#print(csv_data)

#Working with csv file
#with open("iris.csv", "r") as iris_file:  #"r" is the default. This could work the same withour "r"
#   print(iris_file.read()) #Prints the result of reading the file.

#Separating the csv file contents.
with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()  #Readlines reads individual lines. like reading and using the split with "\n".
                                       # Read lines is going to remember the "\n" so it will have to be trimmed.

headers = iris_data[0].strip().split(",") #Strip off excess white space at the end of the line. Using the comma as a delimiting string

irises = []

for row in iris_data[1:]:   #Start not from 0 but from 1. Row 0 is the column headers.
    #sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(",")   # The comma is the delimiting string.
    iris = row.strip().split(",")
    iris_dict = dict(zip(headers, iris))

    irises.append(iris_dict)
    print(iris_dict)
"""iris_dict = {
    "sepal_length": sepal_length,
    "sepal_width": sepal_width,
    "petal_length": petal_length,
    "petal_width": petal_width,
    "species": species
}

irises.append(iris_dict)"""
