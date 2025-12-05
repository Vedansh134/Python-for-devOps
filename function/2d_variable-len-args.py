# Variable-Length Arguments (*args and **kwargs)
# Used when you don't know the exact number of arguments a function will receive [1].
# ------- *args: Collects an arbitrary number of positional arguments into a tuple [1].
# ------- **kwargs: Collects an arbitrary number of keyword arguments into a dictionary [1].

def sum_all(*numbers):
    """Sum all the numbers of args"""
    return sum(numbers)

print(sum_all(1,349,34879,34870))

