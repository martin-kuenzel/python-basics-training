#!/usr/bin/python3
import os

#dir(os) ## will show us all the methods, attributes etc.

print(f'''
os.getcwd() = {os.getcwd()}
''')

#os.mkdir('./created_by_python_basics_os_module.py')
#os.makedirs('./created_by_python_basics_os_module.py2/with_subdir')

#os.rename('./created_by_python_basics_os_module.py','./created_by_python_basics_os_module.py_renamed')

#os.rmdir('./created_by_python_basics_os_module.py_renamed')
#os.removedirs('./created_by_python_basics_os_module.py2/with_subdir')

from datetime import datetime
print(f'''
os.stat('python_basics_os_module.py') = {os.stat('python_basics_os_module.py')}
datetime.fromtimestamp( os.stat('python_basics_os_module.py').st_mtime ) = {datetime.fromtimestamp(os.stat('python_basics_os_module.py').st_mtime)}
''')

print('''
for dirpath, dirnames, filenames in os.walk('./'):
    print('Current Path: ', dirpath) 
    print('Directories:', dirnames)
    print('Filenames: ', filenames)
''')

for dirpath, dirnames, filenames in os.walk('./'):
    print('Current Path: ', dirpath) 
    print('Directories:', dirnames)
    print('Filenames: ', filenames)

print(f'''
os.environ.get('HOME') = {os.environ.get('HOME')}
os.environ.get('USER') = {os.environ.get('USER')}

os.path.join(os.environ.get('HOME'),'testfile.txt') = {os.path.join(os.environ.get('HOME'),'testfile.txt')}

os.path.basename('/tmp/file_does_not_have_to_exist.txt') = {os.path.basename('/tmp/file_does_not_have_to_exist.txt')}
os.path.dirname('/tmp/file_does_not_have_to_exist.txt') = {os.path.dirname('/tmp/file_does_not_have_to_exist.txt')}

os.path.exists('/tmp/file_does_not_have_to_exist_but_if_not_will_return_false.txt') = {os.path.exists('/tmp/file_does_not_have_to_exist_but_if_not_will_return_false.txt')}

os.path.splitext('/tmp/file_does_not_have_to_exist.txt') = {os.path.splitext('/tmp/file_does_not_have_to_exist.txt')}

''')

