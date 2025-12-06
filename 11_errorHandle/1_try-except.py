# The Basic try...except Structure

# The most fundamental way to handle an exception is with try and except blocks.
# The code that might cause an error is placed inside the try block.
# If an error occurs in the try block, the execution stops, and control is passed to the except block.
# The code inside the except block handles the error.

try:
    numerator = 10
    denominator = 0
    result = numerator/denominator
    print(f"{result}")
except:
    print("Error : ZeroDivisionError, \nproblem in try block")
