""" The module package looks through its folder and imports all modules """

import os

potential_modules = os.listdir('.')

for filename in potential_modules:
    if(filename != "__init__.py" and filename[len(filename) - 2:] == "py"):
        __import__(filename[0:len(filename) - 3])
