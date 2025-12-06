## file operations in Python
- A program uses memory to store data temporarily while it is running.
- The random-access memory is volatile, and all its contents are lost once a program terminates. In order to persist the data forever, we use files.
- A file is data stored in a storage device. A python program can talk to the file by reading
content from it and writing content to it.

- A file can be of different types like text files, binary files, image files, audio files, etc.
- In this module, we will focus on text files and binary files.

- File operations in Python, also known as file handling, involve basic actions like creating, reading, writing, and deleting files. These operations use the built-in open() function and a file object to interact with external files.


### Core File Operations
- The basic workflow for file handling involves three primary steps: opening the file, performing an operation, and closing the file.

1. **openning a file** : use open() function
2. **performing file operations** : read(), write(), append()
3. **closing a file** : close() method
4. **with statement** : context manager for file operations
5. **file modes** : read, write, append, binary modes
6. **file methods** : read(), readline(), readlines(), write(), writelines(), seek(), tell()
7. **exception handling** : handling file-related errors
8. **working with different file types** : text files, binary files
9. **file paths** : absolute and relative paths
10. **file manipulation** : os and shutil modules for advanced file operations

## File Access Modes

The mode determines the type of operations you can perform:

| Mode | Description |
|------|-------------|
| `r`  | Read only (default). Raises an error if the file does not exist. |
| `w`  | Write only. Creates a new file if it doesn't exist. If the file exists, its contents are overwritten. |
| `a`  | Append only. Creates a new file if it doesn't exist. New data is added to the end of the existing content. |
| `x`  | Exclusive creation. Creates a new file only if it does not already exist. Raises an error otherwise. |
| `t`  | Text mode (default). Used for handling human-readable characters. |
| `b`  | Binary mode. Used for non-text files like images or audio files (e.g., `rb`, `wb`). |
| `+`  | Update mode. Allows for both reading and writing (e.g., `r+`, `w+`, `a+`). |


### Additional Topics
- File encoding and decoding
- Working with CSV and JSON files
- File compression and decompression
- Best practices for file handling in Python

