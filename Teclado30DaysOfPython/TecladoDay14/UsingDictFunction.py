#Let us create a list with iterables inside.
#In using the dict function, whatever you want to make into a dictionary is passed as an argument

iris = [
    ("sepal_length", "5.1"),
    ("sepal_width", "3.5"),
    ("petal_length", "1.4"),
    ("petal_width", "0.2"),
    ("species", "Iris-setosa")
]

iris_dict = dict(iris) 

print(iris_dict)