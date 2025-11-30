# try block executes :
# The user inputs a valid integer, like 5. The int() conversion works, and denominator becomes 5.
# The division 10 / 5 executes successfully, and result becomes 2.0.

# except blocks are skipped : Since no exception was raised in the try block, the except ZeroDivisionError and except ValueError blocks are entirely ignored.

# else block executes : Because the try block completed without issue, the else block runs, printing "Result is: 2.0".
# finally block executes : The code in the finally block always runs. It prints "Execution finished.".


try:
    numerator = 24
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ValueError:
    print(f"Please enter the correct value for denominator")
except ZeroDivisionError:
    print(f"Please enter the non zero digit for denominator")
else:
    print(f"Result : {result}")
finally:
    print("Execution finished!!")
