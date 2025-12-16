# attributes

# 2 types -
# class.attr - own by class and common for all objects
# obj.attr - instance attribute diff for diff object ex : diff stu (object) name and defined by self.

# ex. of class.attr - all student have same college name
# stroe single time in class

class Student:
    college_name = "IIMT University"
    # not defined by self so it store in memory only one time

    name = "anonymous" # class.attr

    def __init__(self,name):
        self.name = name # obj.attr > class.attr

s1 = Student("Vedansh")
print(f"{s1.name} is studied in {s1.college_name}")
# also valid
print(Student.college_name)

s2 = Student("tejas")
print(f"{s2.name} is studied in {s2.college_name}")

# name is diff for diff object so store in diff times in memory
# But college is same for every student so it store one time

s3 = Student()
print(f"Student name : {s3.name}") # gives error


# we can store two things (collection of two things) in class data (attributes) and other is methods
# attributes - what are properties
# methods - What are you do kya kya kar satke ho (functions)
# ------ Methods are functions that belongs to objects


