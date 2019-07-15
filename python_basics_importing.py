#!/usr/bin/python3
#import python_basics_importing_module ## THIS DOES NOT WORK FOR CALLING FUNCTIONS IN MODULE DIRECTLY (you would need python_basics_importing_module.find_index)
#from python_basics_importing_module import * ## IS ALSO VALID BUT IS PROBLEMATIC BECAUSE ONE DOESN'T KNOW EXACTLY WHERE SOMETHING RESIDES
#from python_basics_importing_module import find_index as f_index, test_string ### FROM SAME DIRECTORY WHERE THIS SCRIPT RESIDES

import sys
sys.path.append('modules') ## WE ADDED A PATH ./modules for additional modules

from python_basics_importing_module import find_index as f_index, test_string ### FROM SAME ./modules SUBDIRECTORY FROM WHERE THIS SCRIPT RESIDES

### PYTHON LOOKS AT THIS LOCATIONS FOR MODULES
#print(sys.path)

courses = ['History','Math','Physics','Biology']

#print(find_index)
#print( find_index(courses,'History') )
print( f_index(courses,'Physics') )

### USING BUILTIN LIBRARIES
import random

print(f'''
import random
random.choice(courses) = {random.choice(courses)}
random.choice(courses) = {random.choice(courses)}
random.choice(courses) = {random.choice(courses)}
random.choice(courses) = {random.choice(courses)}
''')

import math
print(f'''
import math
math.sin(3) = {math.sin(3)}
math.sin(6) = {math.sin(6)}
math.cos(2) = {math.cos(2)}
''')

import datetime
import calendar
print(f'''
import datetime
import calendar
datetime.date.today() = {datetime.date.today()}
calendar.isleap(2019) = {calendar.isleap(2019)}
calendar.isleap(2020) = {calendar.isleap(2020)}
''')

import os
print(f'''
import os
os.getcwd() = {os.getcwd()}
os.__file__ = {os.__file__}
''')

#import antigravity
#print('''
#    import antigravity
#''')
