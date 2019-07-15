#!/usr/bin/python3

### IF/ELIF/ELSE
print(f'''### IF/ELIF/ELSE
if 1 > 2:
    print('1 > 2 ?')
elif 1 < 2:
    print('1 < 2 !')
else:
    print('1 == 2 ?')
''')

if 1 > 2:
    print('1 > 2 ?')
elif 1 < 2:
    print('1 < 2 !')
else:
    print('1 == 2 ?')

print(f'''
list_1 = [1,2,6,7]
if 2 in list_1 and 8 in list_1:
    print('2 and 8 are in list_1')
elif 2 in list_1 and 7 in list_1:
    print('2 and 7 are in list_1')
''')

list_1 = [1,2,6,7]
if 2 in list_1 and 8 in list_1:
    print('2 and 8 are in list_1')
elif 2 in list_1 and 7 in list_1:
    print('2 and 7 are in list_1')

print(f'''
list_1 = [1,2,6,7]
if 2 in list_1 or 8 in list_1:
    print('2 or 8 is in list_1')
''')
list_1 = [1,2,6,7]
if 2 in list_1 or 8 in list_1:
    print('2 or 8 is in list_1')

print(f'''
list_1 = [1,2,6,7]
if 8 not in list_1:
    print('8 is not in list_1')
''')
list_1 = [1,2,6,7]
if 8 not in list_1:
    print('8 is not in list_1')


print(f'''
list_1 = [1,2,6,7]
list_2 = [1,2,6,7]
if id(list_1) == id(list_2):
    print('list_1 is list_2')
elif list_1 is list_2:
    print('list_1 is list_2')
elif list_1 == list_2:
    print('list_1 equals list_2')
''')
list_1 = [1,2,6,7]
list_2 = [1,2,6,7]
if id(list_1) == id(list_2):
    print('list_1 is list_2')
elif list_1 is list_2:
    print('list_1 is list_2')
elif list_1 == list_2:
    print('list_1 equals list_2')

print(f'''
list_1 = [1,2,6,7]
list_2 = list_1
if list_1 is list_2:
    print('list_1 is list_2')
''')
list_1 = [1,2,6,7]
list_2 = list_1
if list_1 is list_2:
    print('list_1 is list_2')

### FOR LOOP
print(f'''
### FOR LOOP
nums = [1,3,5,2,6,1]
for c in nums:
   if c == 3:
       continue 
   if c == 6:
       break
    print(c)
''')

nums = [1,3,5,2,6,1]
for c in nums:
    if c == 3:
        continue 
    if c == 6:
        break
    print(c)

print(f'''
    #### FOR LOOP RANGE
    for i in range(1,5):
        print(i)
''')
    #### FOR LOOP RANGE
for i in range(1,5):
    print(i)

print(f'''
    #### NESTED FOR LOOP
    for i in range(1,5):
        for c in ['a','b','c','d']: do
            print(i + ' ' + c)
''')
    #### NESTED FOR LOOP
for i in range(1,5):
    for c in ['a','b','c','d']: 
        print(f'{i} {c}')

print(f'''
    #### FOR LOOP ENUMERATED
    for c in enumerate(nums):
        print(c)
''')

    #### FOR LOOP ENUMERATED
for c in enumerate(nums):
    print(c)

### WHILE LOOP

print('''
### WHILE LOOP

x = -1

while x < 10:
    if x == 7:
        break

    x+=1
    
    if x == 5: continue

    print(x)
''')

x = -1

while x < 10:
    if x == 7:
        break

    x+=1
    
    if x == 5: continue

    print(x)

print(f'''
    #### INFINITE WHILE LOOP (don't forget to add a break condition)
    while True:
        print(x)
        x+=1
        if x > 20:
            break;
''')

    #### INFINITE WHILE LOOP (don't forget to add a break condition)
while True:
    print(x)
    x+=1
    if x > 20:
        break;

