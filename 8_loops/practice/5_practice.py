# 5. Write a program to find the sum of first n natural numbers using for loop.

# total = 0 gives an error

def sum_no(num):
    total = 0
    for no in range(1,num+1):
        total += no

    print(f"User enter no. {num} and sum : {total}")

def main():
    try:
        number = int(input("Enter no. : "))
        sum_no(number)
    except ValueError:
        print(f"User enter incorrect value. Not an integer")

main()