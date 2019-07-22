#!/usr/bin/python3
list_0 = [2,445,2,65,2,7,2,123,67]
set_0  = {5,2,63,213,276,23,6,2,3}
tup_0  = (2,4,5,2,3,5,6,2,1,45,52)
dict_0 = {"Name":"Doe", "Firstname":"John", "Age": 34}

## SORTING LIST
print( sorted(list_0) ) # the original variable is not affected, but we'll get a new sorted list

print(list_0)
list_0.sort(reverse=True) # will sort the original variable and return None
print(list_0)

# Sorted works not only on lists

## SORTING SETS
print()
print( sorted(set_0) )

## SORTING TUPLES
print()
print( sorted(tup_0) )

## SORTING DICTS
print()
print(list(dict_0.keys()))
for val in dict_0:
    print( dict_0[val] )
print( sorted(dict_0) )
for val in sorted(dict_0):
    print( dict_0[val] )

print()

## Advanced sorting with given keys
print( sorted([-2,5,-15,5,-23]) )
print( sorted([-2,5,-15,5,-23],key=abs) ) ## because of the abs, the absolute values of the numbers are sorted 

print()

## SORTING OBJECTS (a key needs to be given in any case)
class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return f'{self.name},{self.age},${self.salary}'

emp_0 = Employee('John Doe',23,1203)
emp_1 = Employee('Jack Miller',52,4003)
emp_2 = Employee('Susan Starr',35,2032)

## using a lambda (anonymous) function
print( sorted( [emp_0,emp_1,emp_2], key = lambda emp: emp.salary, reverse = True ) )

## using a builtin module operator.attrgetter
from operator import attrgetter
print( sorted( [emp_0,emp_1,emp_2], key = attrgetter('salary'), reverse = True ) )