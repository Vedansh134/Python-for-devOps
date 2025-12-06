## Loops in python

- Loops in Python are used to execute a block of code repeatedly as long as a given condition is true.
- This is essential for tasks requiring repetition, such as iterating through collections or performing operations until a condition changes.

## Types of Loops

- Python primarily uses two types of loops: `while` loops and `for` loops.

- **While Loop** : Repeats a block of code as long as a specified condition is truecd .

    Example :
    ```python
    count = 0
    while count < 5:
        print(f"Count is: {count}")
        count += 1
    ```

- **For Loop** : Used for iterating over a sequence (like a list, tuple, dictionary, set, or string).

    Example :
    ```python
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)
    ```

## Iterating with range()
- use the range() function to generate a sequence of numbers.

    Example :
    ```python
    for i in range(5):
        print(i)
    ```

## Loop Control Statements

- `break` : Exits the loop prematurely when a certain condition is met.
- `continue` : Skips the current iteration and moves to the next iteration of the loop.
- `pass` : A placeholder that does nothing; it can be used when a statement is syntactically required but no action is needed.

## Common Use Cases

- Iterating through lists, tuples, or dictionaries.
- Performing repetitive tasks until a condition changes.
- Processing data in batches.
- Implementing algorithms that require repeated operations.
