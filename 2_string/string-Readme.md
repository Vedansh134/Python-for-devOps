# Strings in Python

- In Python, a string is an immutable sequence of Unicode characters used to store and manipulate text data. Strings are created by enclosing characters in single quotes ('...'), double quotes ("..."), or triple quotes ("""...""" or '''...''') for multiline strings. Python provides a rich set of built-in methods to perform common operations on strings.

## Key Characteristics

- Text Data Type: Strings are primarily used to represent and manipulate text data.
- Immutable: Once a string is created, it cannot be changed. Any method that appears to modify a string actually returns a new string with the changes applied, leaving the original string intact.
- Sequence: Strings are ordered sequences, supporting indexing (accessing individual characters using []) and slicing (extracting substrings using [:])
- Unicode Support: Python 3 strings are Unicode by default, allowing for a wide range of characters from different languages and symbol sets.
- Versatile: Strings can be concatenated, repeated, and formatted in various ways.

# Common String Methods

- Python string methods can be categorized by their functionality. Here are some of the most commonly used string methods grouped by their purpose :

| Category              | Method(s)                                          | Description                                                        |
|----------------------|----------------------------------------------------|--------------------------------------------------------------------|
| **Case Conversion**   | `lower(), upper(), capitalize(), title(), swapcase(), casefold()` | Change the casing of characters within the string.                 |
| **Stripping/Trimming**| `strip(), lstrip(), rstrip()`                      | Remove leading and trailing whitespace or specified characters.     |
| **Searching/Finding** | `find(), index(), count(), startswith(), endswith()` | Locate substrings, count occurrences, or check prefixes/suffixes.  |
| **Modifying/Transforming** | `replace(), join(), split(), splitlines()`      | Replace parts of a string, combine elements from an iterable, or divide the string into a list. |
| **Formatting/Padding**| `format(), center(), ljust(), rjust(), zfill()`   | Format values into a string using placeholders or align/pad the string with specified characters. |
| **Checking Conditions**| `isalnum(), isalpha(), isdigit(), isspace(), islower(), isupper(), istitle()` | Return a boolean (True or False) based on the content of the string. |

## Common String Operations

- Concatenation: Combining strings using the + operator.
- Repetition: Repeating strings using the * operator.
- Slicing: Extracting substrings using indexing and slicing syntax.
- Methods: Python provides numerous built-in string methods for various operations, such as:
  - `str.lower()`: Converts all characters to lowercase.
  - `str.upper()`: Converts all characters to uppercase.
  - `str.strip()`: Removes leading and trailing whitespace.
  - `str.replace(old, new)`: Replaces occurrences of a substring with another substring.
  - `str.split(separator)`: Splits the string into a list of substrings based on a specified separator.
  - `str.join(iterable)`: Joins elements of an iterable (like a list) into a single string, separated by the string on which it is called.
  - `str.find(substring)`: Returns the lowest index of the substring if found, otherwise -1.
  - `str.format()`: Formats the string using placeholders.
- f-Strings: Introduced in Python 3.6, f-strings provide a way to embed expressions inside string literals using curly braces {}.