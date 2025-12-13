# constructors = _init_ function
# All classes have a function called _init_(), which is always executed when the object is being initiated.

# meanswhen you use class to make object so auto. init function called.

class Skills:
    tech = "cloud"
    skill = "AWS"
    # self invoked
    # further more constructor are of two types :-

    # below const. called default constructor
    def __init__(self):
        print(self) # agar hum nahi banaeye ge toh python self bana lega
        pass

    # parameterized constructor (means other p/m other than self)
    def __init__(self,fname,marks):
        self.name = fname
        self.marks = marks
        print("Adding new student on db")

# s1 = Skills() # use () for call the constructor.
# print(s1.skill)
# print(s1.tech)
# print(s1) # <__main__.Skills object at 0x000002B42F09A180> same as self

# Constructor always take a parameter == self (means jo new object create ho rahi hai s1)
# also take multiple parameters after self

s2 = Skills("Vedansh", 100)
print(f"{s2.name} have {s2.marks} marks")

s3 = Skills("devansh", 100)
print(f"{s3.name} have {s3.marks} marks")

# ... nth students

# create object --- then constructor ---- inside pass arg (self) otherwise error (any name).
# with the help of self parameter we can store diff-diff variables/data.
# all store data inside the class/object these variables called attributes.

# So create class
# inside class create constructor
# In const. during making of an object, we can also pass additional infomation like vedansh,100 so these add. information , object ke sath jakar store ho jaye
# and kal ko hum inhe object se inko hum uss info. ko access kr satke hai and use them

# find adv. of using obj.-class we can also use function, we can also used string, dict. to store these values

# --------------------- Also one class ==== 2 contructor so call only object that match with parameters

