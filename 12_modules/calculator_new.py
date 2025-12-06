# What is a Python module?

# A module is just a file containing Python code (functions, classes, variables, and runnable code) that you can reuse in other programs.
# The file name is the module name with a .py extension. For example, a file named math_tools.py is a module called math_tools. modules is a group of functions.

# Why use modules?
# Reusability: Put common functionality in a module and reuse it across many scripts.
# Organization: Break large programs into smaller, logical pieces.
# Collaboration: Share modules with teammates and build on top of standard libraries.
# Maintainability: Update behavior in one place without changing every script.
import sys
import os
#to read env vae

num1 = 234
num2 = 456

def add(num1,num2):
    sum = num1 + num2
    return sum
    #print(f"Addition : {sum}")

def sub(num1,num2):
    sub = num2 - num1
    return sub

def div(num1,num2):
    div = num1/num2
    return div

def mul(num1,num2):
    mul = num1*num2
    return mul

#passing via command line arguements
#bydefault argv read as string
#when you deal with sensitive information so go with environment variables
#keep your information private not public
num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

#invoking the functions
if operation == "add":
    output = add(num1,num2)
    print(output)
if operation == "mul":
    output = mul(num1,num2)
    print(output)
if operation == "div":
    output = num1/num2
    print(output)
if operation == "sub":
    output = num1-num2
    print(output)


# type on export password="vedansh" on console
# env = os.getenv("HOME")
# print(env)
print(os.getenv("HOME"))

#addition(564,675)
#add = addition(5876,4985)
#print(add)

# print(addition(56,675))
# print(subtraction(565,76))
# print(divison(34,54))



# functions
#      Take inputs
#      Perform the request logic
#      Return the output