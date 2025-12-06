# A nested for loop in Python is a loop inside another loop. The inner loop executes completely for every single iteration of the outer loop.
# This structure is commonly used to work with two-dimensional data structures, like matrices, or when you need to combine every element from one list with every element from another.


# ==================================== Example 1: Creating a Grid or Matrix
# This common example demonstrates how nested loops can print a grid pattern.
# We print without a newline character using end=" "

# outer loop iterates 3 times
for row in range(1,4):
    # inner loop iterates 4 times (columns) for each row iteration
    for col in range(1,5):
        print(f"({row},{col})", end="")
    # for print empty line and start with a new line
    print()



# ==================================== 2. Iterating Over Nested Lists (2D Arrays)
# A common use case is processing elements in a list that contains other lists

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    for number in row:
        print(number, end=" ")
    print()

# ==================================== 3. Generating Combinations
# Nested loops are excellent for creating all possible pairings between items from two different sequences.

adjectives = ["red","tasty","juicy"]
fruits = ["cherry","rasberry","berries"]

for adj in adjectives:
    for fru in fruits:
        print(f"{adj,fru}")
    print()
