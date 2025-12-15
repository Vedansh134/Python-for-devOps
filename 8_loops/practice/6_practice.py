# 6. Write a program to calculate the factorial of a given number using for loop

def factorial(number):

    if number < 0:
        print("Factorial is not defined for negative number!")
        return None # FOR INVALID VALUE

    res = 1
    for i in range(1, number+1):
        res = res * i

    return res

def main():
    input_str = (input("Enter a non-negative number that you want to calculate the factorial : "))

    try:
        input_num = int(input_str)
        result = factorial(input_num)
        if result is not None:
            print(f"Factorial of {input_num} : {result}")

    except ValueError:
        print(f"Invalid value! : {input_str}\n Must be integer")

if __name__ == "__main__":
    main()