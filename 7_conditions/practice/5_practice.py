# 5. Write a program which finds out whether a given name is present in a list or not.

name = input("Enter name of user : ")

def check_name(n1):
    list = ["vedansh","devansh","nanu","devu"]

    if n1 in list:
        print(f"{n1} is present inside list")
    else:
        print(f"{n1} is not present inside list")

check_name(name)


