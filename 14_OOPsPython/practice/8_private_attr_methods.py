# Private attributes and methods define
# Use __ to make private and it scope fixed till class only not accessed outside the class
# they are like private but not exactly private in python
# Private attributes & methods are meant to be used only within the class and are not accessible from outside the class
# prevent the expose of attr and methods

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        # call easily due to it present inside the class
        print(self.__acc_pass)

    # define a private method
    def __private_method(self, pri):
        self.priv = pri
        print(self.priv)


acc1 = Account("34809", "abcde")

print(acc1.reset_pass())

# bad practice due to security issues
# so define as private scope till class
print(acc1.acc_no)

# print(acc1.__acc_pass) # gives an error

# print(acc1.__private_method()) # error


print("practice another ...")

class Person:
    # define a private attributes
    __name = "anonymous"

    # define a private method
    # we define this function so any internally function used this function
    def __hello(self):
        print("hello secret")

    def welcome(self):
        # self.__hello(self.__name)
        self.__hello()

p1 = Person()
# print(p1.__name) # gives an error

# print(p1.__hello) # gives an error

print(p1.welcome())
