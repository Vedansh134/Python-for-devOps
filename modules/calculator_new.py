# What is a Python module?

# A module is just a file containing Python code (functions, classes, variables, and runnable code) that you can reuse in other programs.
# The file name is the module name with a .py extension. For example, a file named math_tools.py is a module called math_tools. modules is a group of functions.

# Why use modules?
# Reusability: Put common functionality in a module and reuse it across many scripts.
# Organization: Break large programs into smaller, logical pieces.
# Collaboration: Share modules with teammates and build on top of standard libraries.
# Maintainability: Update behavior in one place without changing every script.

num1 = 234
num2 = 456

def addition(num1,num2):
    sum = num1 + num2
    return sum
    #print(f"Addition : {sum}")

def subtraction(num1,num2):
    sub = num2 - num1
    return f"subtraction : {sub}"

#addition(564,675)
#add = addition(5876,4985)
#print(add)

print(addition(56,675))
print(subtraction(565,76))


# functions
#      Take inputs
#      Perform the request logic
#      Return the output