# Inheritance in oops
# When one class (child/derived) derives the properties & methods of another class (parent/base)

class Car_properties:
    color = "black"
    @staticmethod
    def start():
        print("To start the car...")

    @staticmethod
    def stop():
        print("To stopped the car...")

class Car(Car_properties):
    def __init__(self, name):
        self.name = name

car1 = Car("Audi")
car2 = Car("BMW")

print(car1.name)

# Not get a error
# because all the methods of parent class (Car_properties) is inherit by child class (Car)
print(car1.start())
print(car2.stop())

print(car1.color)

# 1. above is single level inheritance (single child and parent)
# 2. multi-level inheritance base ---> derived ----> derived ...nth...
# 3. multiple inheritance     one class derived properties from many parent/base class