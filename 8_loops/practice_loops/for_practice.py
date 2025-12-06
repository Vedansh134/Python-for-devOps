# 1. Write a program to print multiplication table of a given number using for loop.
# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# 3. Attempt problem 1 using while loop.
# 4. Write a program to find whether a given number is prime or not.
# 5. Write a program to find the sum of first n natural numbers using while loop.
# 6. Write a program to calculate the factorial of a given number using for loop.

# sum
total = 0
for n in range(1,101):
    #total = total+n
    total+=n
    print(f"sum of 55 no. : {total}")

# multiplication
no = int(input("Enter number : "))
for i in range(1,11):
    mul = no*i
    print(f"{no} * {i} = {mul}")


# factorial
fact = int(input("Enter factorial no : "))
res = 1
for i in range(1,fact+1):
    res = res*i
    print(f"factorial of {i} : {res}")
print(f"factorial : {res}")


# reverse multiplication table
n = int(input("Enter no : "))
mul = 1
for i in range(10,0,-1):
    mul = n*i
    print(f"{n} * {i} = {mul}")


# list name filtering
names = ["Aarav", "Bhuvan", "Ananya", "bhavana", "Aditya", "bhavesh", "Akanksha", "Bani", "Aishwarya", "bipin", "Aditi", "bikram"]
for name in names:
    if name.startswith("a") or name.startswith("A"):
        print(f"names start with A/a : {name}")
    else:
        print(f"names start with B/b : {name}")



