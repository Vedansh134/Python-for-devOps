# create class
class Skill:
    skills = "AWS"
    tech = "devOps"

    # default constructor
    def __init__(self, name):
        self.fname = name
        print(self)
        pass

    def stu(self):
        print(f"Student name : {self.fname} and know skill : {self.skills}")

# create object of a class
s1 = Skill("Vedansh kumar")
print(s1.skills)
print(s1.stu())