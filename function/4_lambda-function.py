# Anonymous Functions (Lambda Functions)
# Small, single-expression functions that do not require a def statement. They are defined using the lambda keyword and are often used when a function is required for a short duration (e.g., with filter(), map(), sorted()).

# Standard function
def muliply_by_two(x):
    return x * 2

# Equivalent lambda function
multiply = lambda x: x*100
print(multiply(346870))
