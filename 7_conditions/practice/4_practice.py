# 4. Write a program to find whether a given username contains less than 10 characters or not.

name = input("Enter your name : ")

def username():
    if len(name) < 10:
        print(f"Given username contains less than 10 characters : {name} ")
    else:
        print(f"Given username have more than 10 characters : {name} ")

username()