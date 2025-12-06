# if-elif-else condition in python is used to execute one block of code among multiple conditions.

marks = int(input("Enter your marks : "))

if marks >= 90 and marks < 100:
    print("Grade : A")
elif marks >= 80 and marks < 90:
    print("Grade : B")
elif marks >= 70 and marks < 80:
    print("Grade : C")
elif marks >= 60 and marks < 50:
    print("Grade : D")
elif marks >= 50 and marks < 40:
    print("Grade : E")
else:
    print("Either you enter wrong marks OR Grade : E && FAIL!!")

print("This statement is always run")