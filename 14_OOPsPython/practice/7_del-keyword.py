# When we define/create any objects so it occupy some space in memory due to object's related methods, their attributes - so these things take space in memory
# del keyword - User to delete object properties or object itself.
# used del keyword to delete object

class Student:
    def __init__(self, name):
        self.name = name

stu1 = Student("Vedansh kumar")
print(stu1.name)

del stu1
print(stu1) # gives an error