# function in python
- A function is a resuable block of code that performs specfic , related action.
- Functions help to break our program into smaller and modular chunks.
- Functions improve code reusability and readability.
- Not recommended to write codes many times, You define that code in a fucntion and call that function when required.
- Functions promote code reusability (DRY principle: Don't Repeat Yourself).

## Defining a Function
- In Python, a function is defined using the `def` keyword followed by the function name and parentheses `()`.
- The function body is indented below the function definition line.

```python
def function_name(parameters...):
    # Function body
    # code tio be executed
    result = parameters * 2
    return result
```

## Calling a Function
- To execute a function, you call it by its name followed by parentheses `()`, passing any required arguments.

```python
output = function_name(arguments...)
print(output)
```

## Function Parameters and Arguments
- Parameters are the variables listed in the function definition.
- Arguments are the values passed to the function when it is called.
- Python supports different types of function parameters:
1. Positional Parameters: Arguments are passed in the same order as the parameters are defined.
2. Keyword Parameters: Arguments are passed using the parameter names, allowing for out-of-order passing
3. Default Parameters: Parameters can have default values, which are used if no argument is provided during the function call.
4. Variable-length Parameters: Using `*args` for non-keyword variable-length arguments and `**kwargs` for keyword variable-length arguments.

## Return Statement
- The `return` statement is used to exit a function and return a value to the caller
- If no return statement is used, the function returns `None` by default.

## Function Scope
- Variables defined inside a function are local to that function and cannot be accessed outside of it.
- Variables defined outside a function are global and can be accessed inside the function unless shadowed by a local variable with the same name.

## lambda Functions
- Lambda functions are small anonymous functions defined using the `lambda` keyword.
- They can take any number of arguments but can only have a single expression.
