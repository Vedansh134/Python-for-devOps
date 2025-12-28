# 6. Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F


def check_grades(marks):
    if marks > 100 or marks < 0:
        return "Invalid marks! Please enter marks between 0 and 100."

    if marks == 100:
        print(f"Your score : {marks} Excellent!!")
    elif marks >= 90 and marks <= 99:
        print(f"Your score : {marks} and your grades : A ")
    elif marks >= 80 and marks < 90:
        print(f"Your score : {marks} and your grades : B ")
    elif marks >= 70 and marks < 80:
        print(f"Your score : {marks} and your grades : C ")
    elif marks >= 60 and marks < 70:
        print(f"Your score : {marks} and your grades : D ")
    elif marks >= 50 and marks < 60:
        print(f"Your score : {marks} and your grades : E ")
    elif marks >= 40 and marks < 50:
        print(f"Your score : {marks} and your grades : F ")
    else:
        print(f"Your score : {marks} and Unfortunately You are fail!")

try:
    marks = int(input("Enter your marks : "))
    grade = check_grades(marks)

    if grade == "Invalid marks! Please enter marks between 0 and 100.":
        print(f"{grade} : You type wrong value")
    # else:
    #     print(f"Your score : {marks} and your grade : {grade}")

    # Additional feedback
    if marks == 100:
        print(f"You have excellent score : {marks}")
    elif marks < 40:
        print(f"You need practice and work hard !! : {marks}")

except ValueError as e:
    print(e)
    print(f"Please type marks as an integer value")
except KeyboardInterrupt:
    print("User abrupt the program")