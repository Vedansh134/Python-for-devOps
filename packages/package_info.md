-- What is a Python module?

- A module is just a file containing Python code (functions, classes, variables, and runnable code) that you can reuse in other programs.
The file name is the module name with a .py extension. For example, a file named math_tools.py is a module called math_tools.
Why use modules?

#Reusability    : Put common functionality in a module and reuse it across many scripts.
#Organization   : Break large programs into smaller, logical pieces.
#Collaboration  : Share modules with teammates and build on top of standard libraries.
#Maintainability: Update behavior in one place without changing every script.


-- Two main kinds of modules:

- Built-in standard library modules: Python comes with a large set of modules installed by default (like math, os, datetime, json). You don’t need to install anything extra.

- Third-party modules: Modules created by others that you install from the Python Package Index (PyPI) using tools like pip (e.g., requests, numpy, boto3).


---> How to use modules (importing):

Importing a whole module:
        import math
        print(math.sqrt(16)) # 4.0

Importing specific items from a module:
        from math import sqrt
        print(sqrt(16)) # 4.0

Giving a module an alias:
        import numpy as np
        arr = np.array([1, 2, 3])


- Importing everything (not recommended for large projects):
from math import *


Common patterns:

-- Standard library modules for quick tasks:
- os: interact with the operating system
- sys: system-specific parameters and functions
- datetime: date and time handling
- json: work with JSON data
- Jira: jira
- AWS: Boto3
- http: requests

-- Working with files and data:
- csv, json, configparser, pathlib

-- Web requests:
- requests (third-party, very popular)


What is a package?

A package is a directory of modules with an init.py file. It helps organize modules into a hierarchy. For example, a folder named mypkg with init.py and submodules like utils.py and data.py can be imported as:

import mypkg.utils as u
from mypkg import data

- call as package/libraries

# In devops
- We can use packages/modules
call for AWS, Github or jira API's and httpd request

- you can write modules and push modules to python hub/artifactory/PYPI(python package index)