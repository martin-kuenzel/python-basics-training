#!/usr/bin/python3

print('Imported module python_basics_importing_module.py ...')

test_string = 'Test string'

def find_index(search_list,target):
    '''Find the index lf a value in a sequence'''
    for i, value in enumerate(search_list):
        if value == target:
            return i

    return -1

