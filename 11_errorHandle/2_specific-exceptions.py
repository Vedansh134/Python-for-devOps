# try block : Contains the code that might potentially raise an exception.
# ====== except ValueError : This block specifically catches ValueError exceptions, which occur when a function receives an argument of the correct type but an inappropriate value (e.g., trying to convert a non-numeric string to an integer).

# ====== except ZeroDivisionError : This block specifically catches ZeroDivisionError exceptions, which occur when you attempt to divide a number by zero.

# ====== except Exception as e : This is a more general except block that catches any other type of exception not caught by the preceding specific except blocks. The as e part allows you to store the exception object in a variable e, which can then be used to print details about the error. It's crucial to place more specific except blocks before more general ones, as Python will execute the first except block that matches the exception.

# finally block : This block is optional but useful for cleanup operations (like closing files or releasing resources) that should always happen, regardless of whether an exception occurred or not.

try:
    # code that raise error
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    result = num1/num2
    print(f"Result : {result}")
except ValueError:
    print(f"Please type the correct value! Must be integer : {num1} or {num2}")
except ZeroDivisionError:
    print(f"Num2 {num2} must be above 0, Error can not be divide by 0")
except Exception as e:
    # This is a general exception handler for any other unexpected errors
    # It's good practice to catch specific exceptions first, then a general one
    print(f"An unexpected error occurred: {e}")