# A nested for loop in Python is a loop inside another loop. The inner loop executes completely for every single iteration of the outer loop.
# This structure is commonly used to work with two-dimensional data structures, like matrices, or when you need to combine every element from one list with every element from another.

# Example 1: Creating a Grid or Matrix
# This common example demonstrates how nested loops can print a grid pattern.
# We print without a newline character using end=" "

# outer loop iterates 3 times
for row in range(1,4):
    # inner loop iterates 4 times (columns) for each row iteration
    for col in range(1,5):
        print(f"({row},{col})", end="")
    # for print empty line and start with a new line
    print()