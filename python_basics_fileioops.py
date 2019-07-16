#!/usr/bin/python3
import os

# create a testfiles_path in the scripts directory [if not existant]
testfiles_path = os.path.join( os.path.realpath( os.path.dirname(__file__) ), 'testfiles' )
if not os.path.exists( testfiles_path ):
    os.mkdir( testfiles_path )

testfile = os.path.join( testfiles_path, 'file_io.txt' )

### write in "overwrite" mode
opened_file = open(testfile,mode='w', encoding='utf-8')
print('testing file ops',file=opened_file)
opened_file.close()

### write in append mode
opened_file = open(testfile,mode='a', encoding='utf-8')
print( f'''
    Appending more text to the file object of type {type(opened_file)}
    which resides @{os.path.realpath(os.path.dirname(testfile))}
    and was created by {os.path.realpath(__file__)}.
''', file=opened_file)

print( f'''
    And since it's still opened, we can just add more lines at this time.

    And this is what {os.path.realpath(__file__)} looks like:

''', file=opened_file)

### write the contents of this script into the testfile
the_whole_script = open(__file__,mode='r',encoding='utf-8')
for line in the_whole_script:
    print(line,file=opened_file,end='')

the_whole_script.close()
opened_file.close()

### read the contents of the testfile and print each line to std.out
opened_file = open(testfile,mode='r',encoding='utf-8')
for line in opened_file:
    print(line,end='')
opened_file.close()
