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


  --------------------------------------------------

  Pip is Python’s package installer. It’s the tool you use to install, upgrade, and manage third-party libraries and packages from the Python Package Index (PyPI) and other repositories.

Key points:

Installing packages: Running commands like pip install requests adds the library to your Python environment.
Managing versions: You can specify versions, e.g., pip install "requests>=2.25,<3.0", or upgrade with pip install --upgrade numpy.
Virtual environments: It’s common to use pip inside a virtual environment (created with python -m venv env or virtualenv) to keep project dependencies isolated.
Listing and removing: pip list shows installed packages; pip uninstall package-name removes a package.
Requirements files: You can capture dependencies in a file (usually named requirements.txt) and install all of them with pip install -r requirements.txt.
Common commands:

Install a package: pip install package-name
Install a specific version: pip install package-name==1.2.3
Upgrade a package: pip install --upgrade package-name
Freeze installed packages (for a requirements file): pip freeze > requirements.txt
Install from a requirements file: pip install -r requirements.txt
Check pip version: pip --version (or python -m pip --version to be explicit)
Note on Python versions:

In some systems, pip might point to Python 2, while pip3 targets Python 3. If you’re using Python 3, you might run pip3 install ... or use python3 -m pip install ... to be explicit.
