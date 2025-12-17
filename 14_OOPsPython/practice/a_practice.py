# Methods are functions that belong to object
# Functions we write inside the class, functions ----> call methods
# Now till we learn methods for string, list, dictionary in sab ke liye methods kaise aye hai because all are classes like string,list... jinke hum object create karte the , object ke liye hum methods use karte the...

# define class
class Student:
    college_name = "IIMT University"

    # define constructor
    def __init__(self, name, grade):
        self.username = name # define new attributes [1]
        self.marks = grade

    # define a method/function also must pass a arguement
    # Always write self parameter first
    def welcome(self):
        print(f"Welcome student : {self.username}")
        # Now with the use of self we can also use the properties of self
        # like
        print("Use properties of self : ",self.username)

    def get_marks(self):
        return f"{self.marks}"

# Now create object/Instance of above class
s1 = Student("Vedansh kumar","93")
print(s1)
print(f"Student name : {s1.username} and his grades : {s1.marks} and he is studied in {s1.college_name}")

print("")
# call a method
# objectname.methodname()
s1.welcome()

# print get_marks method
print(s1.get_marks())

# constructor bascially for initializtion of object
# Agar hum object ko create karte time kuch kaam karna chate hai toh like define new attributes [1] so that work we do inside the constructor so in this way we can define the constructor default and parameterized
# Always 1st parameter inside constructor is self (means object instance)
# Then we can give different parameters
# Then we can create attributes. Also two types of attributes
# -- a) class attr b) object attr
# Then we can also create methods/function inside class
# Inside class have fuctions call methods , methods class ke functions hote hai