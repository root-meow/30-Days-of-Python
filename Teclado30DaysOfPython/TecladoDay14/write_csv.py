#Working with csv files.
#splitting data

import csv

iris_data = [
{5.1,3.5,1.4,0.2,Iris-setosa},
{4.9,3,1.4,0.2,Iris-setosa},
{4.7,3.2,1.3,0.2,Iris-setosa},
{4.6,3.1,1.5,0.2,Iris-setosa},
{5,3.6,1.4,0.2,Iris-setosa},
{7,3.2,4.7,1.4,Iris-versicolor},
{6.4,3.2,4.5,1.5,Iris-versicolor},
{6.9,3.1,4.9,1.5,Iris-versicolor},
{5.5,2.3,4,1.3,Iris-versicolor},
{6.5,2.8,4.6,1.5,Iris-versicolor},
{6.3,3.3,6,2.5,Iris-virginica},
{5.8,2.7,5.1,1.9,Iris-virginica},
{7.1,3,5.9,2.1,Iris-virginica},
{6.3,2.9,5.6,1.8,Iris-virginica},
{6.5,3,5.8,2.2,Iris-virginica}
]

def write_file(file):
    with open("file.csv", "w") as file_1:
        writer = csv.writer(file_1)
        file_1.write("sepal_length, sepal_width, petal_length, petal_width, species\n")
        writer.writerows([elem.values() for elem in file])

def read_file():
    with open("file.csv", "r") as file_1:
        content = f.readlines()
        for line in content[1:]:
            columns = line.strip().split(",")
            printf(f"sepal_length:{columns[0]}\tsepal_width:{columns[1]}\tpetal_length:{columns[2]}\tpetal_width:{columns[3]}\tspecies:{columns[4]}")