# 1. Write a program to print multiplication table of a given number using for loop.

def multiply(number):
    for num in range(1,11):
        print(f"{number} X {num:2} = {number * num}")

def main():
    try:
        no = int(input("Enter number : "))
        multiply(no)
    except ValueError:
        print("Invalid value. Please enter an integer")


main()
