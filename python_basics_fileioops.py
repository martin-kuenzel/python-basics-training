#!/usr/bin/python3
import os

# create a testfiles_path_out in the scripts directory [if not existant]
script_dir = os.path.realpath( os.path.dirname(__file__) )
testfiles_path_out = os.path.join( script_dir, 'testfiles_output' )
testfiles_path_in = os.path.join( script_dir, 'testfiles_input' )
if not os.path.exists( testfiles_path_out ):
    os.mkdir( testfiles_path_out )

testfile = os.path.join( testfiles_path_out, 'file_io.txt' )

### write in "overwrite" mode
opened_file = open(testfile,mode='w', encoding='utf-8')
print('testing file ops',file=opened_file)
opened_file.close()

### write in append mode
opened_file = open(testfile,mode='a', encoding='utf-8')
print( f'''
    Appending more text to the file object of type {type(opened_file)}
    which resides @{testfiles_path_out}
    and was created by {os.path.join(script_dir,__file__)}.
''', file=opened_file)

print( f'''
    And since it's still opened, we can just add more lines at this time.

    By opening files this way, we must not forget to close the file after operating on it,
    so there has to be a better way to do the IO operatipons.
''', file=opened_file)

### write the contents of this script into the testfile
the_whole_script = open(__file__,mode='r',encoding='utf-8')
# for line in the_whole_script:
#     print(line,file=opened_file,end='')

# the_whole_script.close()
# opened_file.close()

### USING A CONTEXT MANAGER (auto closes file)
with open(testfile,mode='r',encoding='utf-8') as opened_file:
    ### reads only one line from the file, prints that one out and goes to the next line
    #print( opened_file.readline(), end='' )
    
    ### read the contents of the testfile and print each line to std.out (possible ways)
    
    #### bad for large files
    #print(  opened_file.readlines() )
    
    #### efficient way to read all the contents of a file
    #for line in opened_file:
    #    print(line,end='')

    #### reads n characters of a file until no more chars available
    #size_to_read = 100
    #f_contents = opened_file.read(size_to_read)
    #opened_file.tell() ## outputs cursor position
    #opened_file.seek() ## can be used to change the position of the cursor
    #while len(f_contents)>0:
    #    print(f_contents,end='')
    #    f_contents = opened_file.read(size_to_read)
    pass

with open(testfile,mode='a',encoding='utf-8') as f:
    print(f'''
And there it is, the better method to write/append content to a file using context managers
This is what {os.path.join(script_dir,__file__)} looks like:
    ''', file=f)
    ### write the contents of this script into the testfile
    with open(__file__,mode='r',encoding='utf-8') as the_whole_script:
        for line in the_whole_script:
            print(line,file=f,end='')

### write the files content to stdout
with open(testfile,mode='r',encoding='utf-8') as f:
    for line in f:
        print(line,end='')

### copying binary files 
image_file = os.path.join(testfiles_path_in,'face-wink.png')
image_file_copy = os.path.join(testfiles_path_out,'face-wink_copy.png')
with open(image_file,'rb') as img:
    with open(image_file_copy,'wb') as img_copy:
    #    for l in img:
    #        img_copy.write(l)
    #### alternatively
        chunk_size = 2048
        chunk = img.read(chunk_size)
        while len(chunk) > 0:
            img_copy.write(chunk)
            chunk = img.read(chunk_size)

