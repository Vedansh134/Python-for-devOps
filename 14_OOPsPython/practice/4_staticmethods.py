# Static methods are methods that don't use self parameter (work at class level) not on object level
# -- special method
# Pre. self use for objects but, we can create method that not need of object (not pass the attribute of obj.)
# so define these on class level instead of object level
# decorators inside we have @staticmethod and also diff types of decorators

class City:
    def __init__(self, city):
        self.city = city

    # @staticmethod - decorator that convert normal function to be a static method
    @staticmethod
    def greeting():
        print("Bonjour")
    # these are on class level and not req. self p/m so we can use static method decorator

c1 = City("moz")
print(c1.city)

# print(c1.greeting()) gives error [ req. 1 pos. arg ] after apply @st.. method then not any err
print(c1.greeting())