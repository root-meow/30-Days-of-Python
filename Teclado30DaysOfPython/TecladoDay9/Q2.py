#Unpack into 4 variables
#The data represents a student's name, their student id number, and their major and minor disciplines in that order.

student_name, student_id_no, (major, minor) = ("John Smith", 11743, ("Computer Science", "Mathematics"))


print(f"The name is {student_name} with id number {student_id_no} with major in {major} and minor in {minor}")