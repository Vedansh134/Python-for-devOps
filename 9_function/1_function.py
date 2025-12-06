# key components of a function :
# 1. Function Definition : The function is defined using the 'def' keyword followed by the function name and parentheses.
# 2. Parameters : The function 'greet_person' takes one parameter 'greet', which is used to pass a value into the function.
# 3. Function Body : The indented block of code that performs the task of the function. In this case, it creates a greeting message.
# 4. Return Statement : The 'return' statement is used to send the result back to the caller of the function.
# 5. Function Call : The function is called with the argument "Hello", and the result is stored in the variable 'result' and printed.

name = input("Enter your name : ")

def greet_person(greet):
    message = greet+" "+name
    return message

# Calling the function
result = greet_person("Hello")
print(result)

