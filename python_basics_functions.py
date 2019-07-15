#!/usr/bin/python3

print(f'''
### FUNCTIONS

## A function that does nothing
def simple_func():
    pass 

print(simple_func)
print(simple_func())
''')

### FUNCTIONS

## A function that does nothing
def simple_func():
    pass 

print(simple_func)
print(simple_func())

print(f'''
## A function that prints something
def simple_func_2():
    print('I was started')

simple_func_2()
''')

## A function that prints something
def simple_func_2():
    print('I was started')

simple_func_2()

print(f'''
# A function that sums a and b
def math_func_1(a=1,b=1):
    return a + b

num = math_func_1(b=5)
print(num)
num = math_func_1(num,5)
print(num)
num = math_func_1( math_func_1(num,num), num )
print(num)
''')

# A function that sums a and b
def math_func_1(a=1,b=1):
    return a + b

num = math_func_1(b=5)
print(num)
num = math_func_1(num,5)
print(num)
num = math_func_1( math_func_1(num,num), num )
print(num)

print(f'''
#### working with *args == list(arguments)

# A function that builds a product over n values
def math_func_2(*args):
    ret = 1
    if len(args) < 1: return 0
    for i in args:
        ret *= i
    return ret

num = math_func_2(5,2,5)
print(num)
num = math_func_2(num,5)
print(num)
num = math_func_2( math_func_2(num,num), num )
print(num)
''')

# A function that builds a product over n values
def math_func_2(*args):
    ret = 1
    if len(args) < 1: return 0
    for i in args:
        ret *= i
    return ret

num = math_func_2(5,2,5)
print(num)
num = math_func_2(num,5)
print(num)
num = math_func_2( math_func_2(num,num), num )
print(num)

print('\n\n#### working with *args == list(arguments)')
print('#### working with **kwargs == dict(arguments) [kwargs stands for "keyword arguments"]')
print("\n# A function that prints a combined string of a student's info with courses he attends")
print("def stud_info(*courses,**sinfo):")
print("     print(f'{sinfo} is attending the courses')")
print("     print(f'{courses}')")
print("\ncourses = ['Math','Biology','Physics']")
print("student_info = { 'name': 'John', 'age': 26 }")
print("\nstud_info(*courses,**student_info)\n")

# A function that prints a combined string of a student's info with courses he attends
def stud_info(*courses,**sinfo):
    print(f'{sinfo} is attending the courses')
    print(f'{courses}')

courses = ['Math','Biology','Physics']
student_info = { 'name': 'John', 'age': 26 }

stud_info(*courses,**student_info)
