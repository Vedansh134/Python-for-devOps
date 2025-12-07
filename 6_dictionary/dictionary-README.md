# Dictionary

- A dictionary in Python is a built-in, unordered, and mutable collection used to store data values in key-value pairs.
- It is a core data structure that offers highly efficient lookups, insertions, and deletions based on the keys.
- Dictionaries are defined by placing a comma-separated sequence of key: value pairs within curly braces {}
- Keys must be unique and immutable (e.g., strings, numbers, or tuples), while values can be of any data type and can be duplicated.
- Dictionaries are widely used in various applications, including data storage, configuration management, and as a way to represent complex data structures.
- Common operations on dictionaries include adding, updating, and removing key-value pairs, as well as retrieving values based on their keys.
- Python provides several built-in methods for dictionaries, such as `.get()`, `.keys()`, `.values()`, and `.items()`, to facilitate easy manipulation and access to the data stored within them.
- Dictionaries are also used in various Python libraries and frameworks, making them an essential part of Python programming for developers and DevOps professionals alike.

## Key Characteristics

- **Unordered**: Dictionaries do not maintain any order for the key-value pairs.
- **Mutable**: You can change, add, or remove items after the dictionary has been created.
- **Dynamic Size**: Dictionaries can grow and shrink as needed.
- **Key-Value Pairs**: Each item in a dictionary is a pair consisting of a key and a value.
- **Fast Lookups**: Accessing values by their keys is very efficient.

## Different methods in dictionary

- `dict.get(key, default=None)`: Returns the value for `key` if `key` is in the dictionary, else `default`.
- `dict.items()`: Returns a view object that displays a list of dictionary's key-value pairs.
- `dict.keys()`: Returns a view object that displays a list of all the keys in the dictionary.
- `dict.values()`: Returns a view object that displays a list of all the values in the dictionary.
- `dict.pop(key, default=None)`: Removes the specified key and returns the corresponding value. If the key is not found, returns `default` if provided, otherwise raises a `KeyError`.
- `dict.popitem()`: Removes and returns an arbitrary (key, value) pair from the dictionary.
- `dict.update([other])`: Updates the dictionary with the key-value pairs from `other`, overwriting existing keys.
- `dict.clear()`: Removes all items from the dictionary.
- `dict.copy()`: Returns a shallow copy of the dictionary.
- `len(dict)`: Returns the number of items in the dictionary.
- `dict.fromkeys(seq, value)`: Creates a new dictionary with keys from `seq` and values set to `value`.
- `dict.setdefault(key, default=None)`: Returns the value of `key` if it is in the dictionary; if not, inserts `key` with a value of `default` and returns `default`.



