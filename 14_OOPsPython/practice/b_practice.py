# Create student class that takes name and marks of 3 subjects as argurments in constructor.
# Then create a method to print the average.

class Student:
    def __init__(self, name, marks):
        # name and marks is attributes
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hi {self.name}, Your avg score : {sum/5}")

s1 = Student("Vedansh kumar", [89, 84, 86, 78, 84])

# Now call the method inside class
s1.get_avg()

# Also change the value of attribute directly
s1.name = "Nanu"
s1.get_avg()

# Till now we learn methods like get_avg() is non static method (normal)