# Raising Exceptions Manually
# The raise keyword can be used to trigger an exception, useful for validation.

age = int(input("Enter your age : "))

def check_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative {age}. Please give me again")
    print(f"Your age : {age}")

try:
    check_age(age)
except ValueError as e:
    print(f"Error occured : {e}")
