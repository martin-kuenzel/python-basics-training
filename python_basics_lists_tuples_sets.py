#/usr/bin/python3
### Lists
courses = ['History','Math','Physics','Computer Science']
print(f'''
### Lists
courses = {courses}
len(courses) = {len(courses)}
courses[3] = {courses[3]}
courses[-1] = {courses[-1]}
courses[1:3] = {courses[1:3]}
courses[:2] = {courses[:2]}
courses[2:] = {courses[2:]}
''')

courses.append('Psychology')
print(f'''courses.append('Psychology')
courses = {courses}
''')

courses.insert(1,'Art')
print(f'''courses.insert(1,'Art')
courses = {courses}
''')

courses_2 = ['Biology','Chemistry']
courses.insert(0,courses_2)
print(f'''courses_2 = ['Biology','Chemistry']
courses.insert(0,courses_2)
courses = {courses}
''')

courses.remove(courses_2)
print(f'''courses.remove(courses_2)
courses = {courses}
''')

courses.extend(courses_2)
print(f'''courses.extend(courses_2)
courses = {courses}
''')

popped=courses.pop()
print(f'''popped=courses.pop()
popped = {popped}
courses = {courses}
''')

courses.reverse()
print(f'''courses.reverse()
courses = {courses}
''')

courses.sort()
print(f'''courses.sort()
courses = {courses}
''')

courses.sort(reverse=True)
print(f'''courses.sort(reverse=True)
courses = {courses}
''')

sorted_courses = sorted(courses)
print(f'''sorted_courses = sorted(courses)
sorted_courses = {sorted_courses}
courses = {courses}
''')

print(f''''Math' in courses = {'Math' in courses}
'Chemistry' in courses = {'Chemistry' in courses}
''')

num_list = [2,15,6,3,76,2,76,2,1,7,772,223,1]
min(num_list)
max(num_list)
sum(num_list)
num_list_2 = sorted(num_list)
num_list.sort(reverse=True)

print(f'''
num_list = [2,15,6,3,76,2,76,2,1,7,772,223,1]
min(num_list) = {min(num_list)}
max(num_list) = {max(num_list)}
sum(num_list) = {sum(num_list)}

num_list_2 = sorted(num_list,reverse=True)
num_list.sort()

num_list   = {num_list}
num_list_2 = {num_list_2}
''')

print(f'''
for course in courses:
    print(course)
''')

for course in courses:
    print(course)

print(f'''
for idx_course in enumerate(courses):
    print(idx_course)
''')
for idx_course in enumerate(courses):
    print(idx_course)

courses_joined = ' - '.join(courses)
courses_split  = courses_joined.split(' - ')
print(f'''
courses_joined = ' - '.join(courses)
courses_joined = {courses_joined}
courses_split  = courses_joined.split(' - ')
courses_split  = {courses_split}
''')

### Tuples
courses_2 = courses
print(f'''### Tuples (immutable)
    #### Problem with two lists when replacing item in one list it's also replaced in the other one
        courses = {courses}
        type(courses) = {type(courses)}
        courses_2 = courses
        courses_2 == {courses_2}
''')

courses[0] = 'Chemistry'
print(f'''
        courses_2 = courses
        courses[0] = 'Chemistry'
        courses == {courses}
        courses_2 == {courses_2}
''')

courses = ('History','Math','Physics','Computer Science')
print(f'''
    courses = ('History','Math','Physics','Computer Science')
    type(courses) = {type(courses)}

    #### the following is not possible with tuples, because a tuple can not be mutated
        courses[0] = 'Chemistry'
        courses == {courses}
''')

### Sets
courses = {'History','Math','Physics','Computer Science'}
print('### Sets')
print("courses = {'History','Math','Physics','Computer Science'}")
print(f'''type(course) = {type(course)}
    courses == {courses}

    ## Duplicates are removed automatically
''')

courses = {'History','Math','Math','Physics','Computer Science'}
print("\tcourses = {'History','Math','Math','Physics','Computer Science'}")
print(f'\tcourses == {courses}')

courses_2 = {'History','Art'}
print(f'''
    #### comparing Sets
        courses_2 = {courses_2}
        courses = {courses}

        courses.intersection(courses_2) = {courses.intersection(courses_2)}
        courses.difference(courses_2) = {courses.difference(courses_2)}
        courses.union(courses_2) = {courses.union(courses_2)}
''')

### creating empty list,sets,tuples
empty_list = []
empty_list = list()
empty_tuple = ()
empty_tuple = tuple()
#empty_set = {} ### THIS CREATES A DICT, NOT A SET
empty_set = set()
print(f'''### creating empty list,sets,tuples
empty_list = []
empty_list = list()
empty_tuple = ()
empty_tuple = tuple()
#empty_set = '''+'{}'+''' ### THIS CREATES A DICT, NOT A SET
empty_set = set()
''')
