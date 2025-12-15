# 7. Write a program to print multiplication table of n using for loops in reversed order.

def multiple_reverse(num):

    # Iterate from 10 down to 1 (inclusive)
    # range(start, stop, step): 10 is included, 0 is excluded, step is -1
    print(f"\n--- Multiplication Table of {num} (Reversed) ---\n")

    table_lines = []

    for multiplier in range(10, 0, -1):
        product = num * multiplier

        line = f"{num} X {multiplier} = {product}"
        table_lines.append(line)

    return"\n".join(table_lines)

def main():
    input_str = input("Enter number that is integer only : ")

    try:
        input_num = int(input_str)
        result = multiple_reverse(input_num)
        print(f"Multiplication table : {input_str} \n\n{result}")

    except ValueError:
        print(f"Invalid value! Enter must be interger not : {input_str}")

if __name__ == "__main__":
    main()