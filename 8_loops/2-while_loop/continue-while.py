# The continue statement skips the current iteration of the loop. When encountered, Python jumps immediately back to the top of the loop, re-evaluates the condition, and proceeds with the next iteration.

# It is typically used to skip processing of unwanted values or specific conditions while allowing the rest of the loop to run normally.

# =================================== Example: Skipping odd numbers
# Note: It's vital to increment your loop variable (number += 1) BEFORE the continue statement if it might be triggered, otherwise you risk creating an infinite loop.

number = 0
odd_no = []
even_no = []

while number < 10:
    number += 1
    if number % 2 != 0:
        print(f"skipping odd numbers : {number}")
        odd_no.append(number)
        continue

    print(f"processing even numbers : {number}")
    even_no.append(number)

print()
print(odd_no)
print(even_no)