# Abstraction
# Hiding the implementation details of a class and only showing the essentials features to the user.
# hide unneccessary details
# ex : internal process of car start/stop

class Car:
    def __init__(self):
        self.accelerator = False
        self.brk = False
        self.clutch = False

    def start(self):
        # unnesscary defined here inside class, outside class not print unrelevant things
        self.clutch = True
        self.accelerator = True
        print("car started..")

car1 = Car()
car1.start()
