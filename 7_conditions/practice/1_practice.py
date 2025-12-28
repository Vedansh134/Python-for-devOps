# 1. Write a program to find the greatest of four numbers entered by the user.

def max_no(no1,no2,no3,no4):
    if no1 >= no2 and no2 >= no3 and no3 >= no4:
        print(f"No1 is big : {no1}")
    elif no2 >= no1 and no2 >= no3 and no2 >= no4:
        print(f"No2 is big : {no2}")
    elif no3 >= no1 and no3 >= no2 and no3 >= no4:
        print(f"No3 is big : {no3}")
    else:
        print(f"No4 is big : {no4}")

# using the built-in max() function
max_no = max(no1,no2,no3,no4)
print(f"Max no. : {max_no}")
